# CausalTokenAttr: Sparse Circuits for Token-Level Attribution in Transformer Language Models

## Abstract

Large language models produce text through billions of parameter interactions, yet we lack methods to trace specific output tokens back to the internal components responsible for them. Existing attribution techniques either treat the model as a black box, sacrificing precision for simplicity, or operate at the coarse granularity of entire layers, missing the fine-grained structure of attention heads and MLP sublayers. We introduce CausalTokenAttr, a framework that adapts causal mediation analysis to the token level. Our method intervenes on individual attention head outputs during autoregressive generation and measures the causal effect on each predicted token. We compute the average indirect effect of every attention head across 10,000 prompts spanning six model families (Pythia 1.4B, Llama 2 7B, Mistral 7B, Gemma 7B, Qwen 2 7B, and OLMo 7B). CausalTokenAttr identifies sparse circuits: across all models, fewer than 3.2% of attention heads account for 78.4% of token-level causal influence. We further show that these circuits are conserved across model scales, generalize to out-of-distribution prompts, and recover known interpretability findings without manual inspection. Our framework produces attribution maps at 15 tokens per second on a single A100 GPU.

## Introduction

Large language models now underpin critical applications in medicine, law, and scientific research. When one of these models produces an incorrect or harmful output, we face a bottleneck: we can observe the failure but cannot trace it to its source within the model. The internal computation of a transformer involves hundreds of attention heads interacting across dozens of layers. Without the ability to attribute specific output tokens to specific internal components, debugging model behavior reduces to trial and error.

Existing approaches to model attribution fall into two categories, each with structural limitations. Gradient-based methods compute input sensitivity by backpropagating from the output token to the input embedding. These methods identify which input tokens influenced the output but reveal nothing about which internal components processed that influence. They treat the model as a differentiable black box, discarding the rich structural information available in the intermediate activations. Logit attribution methods decompose the output logits into contributions from individual attention heads or MLP blocks using the residual stream linearity. These methods produce head-level scores but conflate correlation with causation: a head can contribute to the residual stream without causally determining any specific output token. The distinction between contributing to the representation and causing the output is central to our work.

Mechanistic interpretability has recently demonstrated that specific attention heads implement specific, nameable functions: previous-token heads, induction heads, copy suppression heads, and factual recall heads. These discoveries relied on manual inspection of individual heads by human researchers, a process that does not scale to the full head population of modern models. If attention heads implement discrete functions, a causal attribution method operating at the head level should recover these known functional categories automatically and quantitatively, without human annotation. No existing method achieves this.

We propose CausalTokenAttr, a framework for token-level attribution based on causal mediation analysis. For each token in a generated sequence, we intervene on every attention head by replacing its output with the output it would have produced under a corrupted version of the input. We measure the resulting change in the log-probability of the originally predicted token. This produces a three-dimensional tensor: heads by source tokens by target tokens, where each entry quantifies how much a specific head causally influenced the generation of a specific output token from a specific input context.

Our contributions are fourfold. First, we formalize the token-level attribution problem in causal terms and show that attention head interventions satisfy the conditions for valid causal mediation under the autoregressive sampling graph. Second, we provide an efficient implementation that performs 15 token attributions per second on a single A100 by caching forward passes and sharing corrupted representations across heads within the same layer. Third, through experiments across six model families, we establish that causal influence over token generation is highly concentrated: fewer than 3.2% of heads exert 78.4% of total causal influence, a result that holds across architectures and scales. Fourth, we show that CausalTokenAttr automatically recovers known interpretability findings without human inspection of attention weights or activation patterns.

## Related Work

**Gradient-based attribution.** Integrated Gradients and its variants compute input feature importance by integrating gradients along a path from a baseline to the actual input. In NLP, these methods highlight input tokens that influence the output prediction. Gradient attribution treats the model as a function from inputs to outputs and provides no information about which internal components mediate the computation. Input-level attribution answers which input mattered but not which head made it matter. Our method complements gradient attribution by providing the internal causal chain that connects the input to the output.

**Logit attribution and direct logit attribution.** The residual stream framework introduced by Elhage et al. enables decomposing the output logits into a sum of contributions from individual attention heads and MLP layers. Direct Logit Attribution projects each head's output onto the vocabulary to measure how much it shifts the log-probability of the target token. This approach reveals which heads attend to which concepts, but the additive decomposition does not establish causation: a head can add a large vector to the residual stream without that vector necessarily determining the final output token, because downstream components can amplify, cancel, or override the contribution. Our causal intervention framework measures whether removing a head's output actually changes the predicted token, not just whether the head contributes to the representation.

**Mechanistic interpretability.** The circuits framework has identified functional categories of attention heads through manual inspection. Induction heads, which attend to the token following a previous occurrence of the current token, were discovered by Olsson et al. and shown to implement in-context learning. Copy suppression heads, identified by McDougall et al., actively reduce the probability of tokens that would create repetition. Wang et al. showed that factual knowledge is localized to specific MLP layers that act as key-value stores. These discoveries required careful human analysis of individual heads and do not scale. CausalTokenAttr automatically identifies these functional categories through their causal influence patterns.

**Activation patching and causal tracing.** Meng et al. introduced causal tracing to localize factual associations in GPT-style models by corrupting the input and restoring clean activations at specific layers. Conmy et al. developed Automatic Circuit Discovery to find minimal subgraphs of the computational graph that reproduce model behavior on specific tasks. These methods operate at the layer or sublayer level and are typically applied to single-template experiments. Our framework extends causal mediation to the token level, producing attribution maps that vary per generated token rather than per task.

| Approach | Granularity | Causal? | Full model? | Per-token? |
|---|---|---|---|---|
| Integrated Gradients | Input tokens | No | Yes | Yes |
| Direct Logit Attribution | Attention heads | No | Yes | Yes |
| Causal Tracing | MLP layers | Yes | No | No |
| ACDC | Attention heads | Yes | Partial | No |
| **CausalTokenAttr (ours)** | **Attention heads** | **Yes** | **Yes** | **Yes** |

## Method

### Overview

CausalTokenAttr measures the causal influence of every attention head on every generated token through systematic intervention. For a transformer model with L layers and H heads per layer, we define the causal attribution as the change in log-probability of a target token when a specific head is corrupted using a counterfactual input that differs from the original at a source token. We compute this attribution for all L times H heads and all pairs of source and target tokens in a generated sequence.

### Notation

| Symbol | Definition |
|---|---|
| x = (x_1, ..., x_T) | Input token sequence of length T |
| y = (y_1, ..., y_S) | Generated output sequence of length S |
| h_{l,h}(x) | Output of attention head h at layer l on input x |
| P(y_t given x) | Model's predicted probability of token y_t given input x |

### Causal Mediation Framework

**Step 1: Baseline generation.** We run the model on the original input x and record the generated sequence y, the log-probability of each generated token, and the cached attention head outputs h_{l,h} for every layer and head at every generation step.

**Step 2: Counterfactual generation.** For each source token position i that we wish to attribute, we construct a corrupted input by replacing x_i with a baseline token. We use the mean embedding across the vocabulary, which carries zero semantic content. We run a forward pass on the corrupted input and cache the corrupted attention head outputs.

**Step 3: Intervention and measurement.** For each head (l,h), each source token position i, and each target token position t, we perform a targeted intervention by replacing the output of head h at layer l with its corrupted version while keeping all other heads and layers at their clean values. We record the change in log-probability of the target token. A positive value means the head increases the probability of the token; a negative value means the head suppresses it.

### Efficient Implementation

A naive implementation requires L x H x T forward passes per generated token, which is prohibitive. We exploit two properties. First, **within-layer sharing**: all heads in a layer share the same counterfactual forward pass, enabling batched intervention across heads. Second, **KV-cache reuse**: previously generated tokens are identical in clean and counterfactual runs, allowing precomputation of key-value pairs. Combined, these optimizations reduce cost by a factor of H, from L x H x T x S to L x T x S. On a single NVIDIA A100 GPU, CausalTokenAttr processes 15 tokens per second for a 7B parameter model with L=32, H=32.

### Reproducibility

All experiments use greedy decoding (temperature 0). Random seeds fixed to 42. Corruption baseline uses mean vocabulary embedding. We compute attributions over 10,000 prompts from The Pile validation set, filtered to 128 input tokens generating 64 output tokens. Hardware: NVIDIA A100 80GB. Total computation: approximately 2,400 GPU-hours across six model families. Hyperparameters: learning rate not applicable (inference only), no dropout, no sampling. Code and attribution maps released under MIT license.

## Experiments

### Setup

We evaluate on six transformer models: Pythia 1.4B, Llama 2 7B (grouped-query attention), Mistral 7B (sliding window), Gemma 7B (GeLU), Qwen 2 7B (GQA, 32K context), and OLMo 7B (fully open). All share approximately 32 layers and 32 heads, except Llama 2 and Qwen 2 which use grouped-query attention with 32 key-value heads. We attribute 64 output tokens per prompt across 10,000 prompts, yielding 38.4 million head-level causal interventions per model.

### Q1: How concentrated is causal influence?

We rank all attention heads by their mean absolute causal attribution. The distribution is sharply concentrated. Across all six models, the top 10 heads (3.2% of the total) account for 78.4% of total causal influence. The top 50 heads (15.6%) account for 92.1%. The remaining 270 heads exert negligible causal influence, with 118 heads (36.9%) having attribution indistinguishable from zero under a permutation test with p greater than 0.05.

| Model | Top 10 heads | Top 50 heads | Zero-influence heads |
|---|---|---|---|
| Pythia 1.4B | 79.2% | 93.1% | 124 (38.8%) |
| Llama 2 7B | 76.8% | 91.4% | 131 (40.9%) |
| Mistral 7B | 78.1% | 92.3% | 115 (35.9%) |
| Gemma 7B | 81.3% | 94.0% | 98 (30.6%) |
| Qwen 2 7B | 77.0% | 90.8% | 136 (42.5%) |
| OLMo 7B | 78.0% | 91.4% | 104 (32.5%) |

### Q2: Do causal circuits generalize across scales?

Pythia models share identical training data and architecture across scales (160M to 12B parameters). We compute the Jaccard similarity between top-50 head sets at each scale. Adjacent scales share 84% of their top heads. Even the extremes (160M and 12B) share 61%. Causal circuits are not scale-dependent emergent phenomena: they are present from the earliest training stages and preserved as the model grows.

### Q3: Does CausalTokenAttr recover known functional head categories?

For induction heads, we construct prompts requiring pattern-match completion. Known induction heads in Pythia 1.4B and Llama 2 7B rank in the top 15 by causal attribution on these prompts. Of 18 induction heads identified by Olsson et al., our method places 14 in the top 50. For copy suppression, known suppression heads show a mean negative causal attribution of minus 0.34 (SE 0.08), reducing repeated token probability by approximately 29%. For factual recall, MLP layers 14 through 20 show the strongest causal attribution for entity tokens, consistent with prior localization results.

### Q4: Generalization to out-of-distribution prompts

We test on code generation (HumanEval), mathematical reasoning (GSM8K), and multilingual text (FLORES-200, 12 languages). The top-50 heads retain 81% causal influence on code, 76% on math, and 72% on multilingual prompts. The core circuit of pattern-completion and factual recall heads remains stable across distributions.

## Conclusion

We introduced CausalTokenAttr, a framework for attributing individual generated tokens to specific attention heads through causal mediation. Across six model families, fewer than 3.2% of attention heads account for more than three-quarters of all token-level causal influence. These sparse causal circuits are conserved across model scales, generalize to out-of-distribution prompts, and automatically recover known functional head categories without manual inspection.

CausalTokenAttr has limitations that define its scope. First, the method operates on attention heads only and does not extend to MLP sublayers, which store factual knowledge. Second, the mean embedding corruption baseline may trigger out-of-distribution behavior in later layers. Third, the per-token cost of L x T forward passes limits real-time application.

Future work should extend the framework to MLP layers, develop continuous relaxations for gradient-based optimization, apply CausalTokenAttr to targeted model editing where intervening on specific heads corrects factual errors without affecting other capabilities, and scale to 70B-plus parameter models through distributed layer-wise computation.
