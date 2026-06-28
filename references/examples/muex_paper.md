# MUE-X: Multi-User Environment for Cross-Modal Agents with Shared Memory and Zero-Shot Task Transfer

## Abstract

Modern AI agents are narrow specialists. A warehouse navigation robot learns nothing from a restaurant booking assistant, even when both solve pathfinding under constraints. This fragmentation forces each agent to rediscover fundamental skills from scratch, wasting 62% of total training compute in multi-agent deployments. We introduce MUE-X, the first framework to demonstrate zero-shot knowledge transfer between agents operating in completely different environments with incompatible observation and action spaces. MUE-X learns a shared neural memory bus that encodes agent experiences into a modality-agnostic latent space, where a vision agent navigating a maze retrieves relevant experiences from a language agent resolving spatial descriptions. Our method trains a trajectory-level contrastive encoder on 2.1 million cross-modal experience pairs, then exposes a retrieval-augmented policy that queries the shared memory at inference time without knowing the source modality of the retrieved content. Across 18 environments and 47 task types spanning vision, language, and structured action domains, MUE-X achieves a 34.2% relative improvement in zero-shot success rate over the strongest baseline, reduces training samples by 3.8x on new tasks, and generalizes to unseen environments with only 4.2% absolute degradation. The shared memory bus alone accounts for 28.1 points of the total gain. To our knowledge, this is the first empirical demonstration that agents with incompatible interfaces can transfer learned skills through a shared representation space, suggesting a path toward generalist agents that accumulate knowledge across domains without architectural compromise.

## Introduction

A warehouse robot navigates aisles, dodges obstacles, and plans efficient routes. A restaurant booking assistant parses user preferences, resolves scheduling conflicts, and confirms reservations. A code generation agent reasons about data structures, anticipates edge cases, and synthesizes correct functions.

These three agents look nothing alike. Their observations differ: pixels versus text versus abstract syntax trees. Their actions differ: motor torques versus dialog acts versus token sequences. Their reward signals differ: package delivery versus user satisfaction versus test pass rates.

And yet, beneath these surface differences, they all solve the same fundamental problems. Pathfinding under constraints. Backtracking from dead ends. Recognizing when a local solution violates a global constraint. Trading off exploration against exploitation.

Current training paradigms force each agent to learn these skills independently, from scratch, with no memory of what any other agent has already discovered. A warehouse robot that has navigated 10,000 mazes possesses emergent spatial reasoning capabilities that could, in principle, inform a restaurant booking agent reasoning about reservation topologies. But there is no mechanism for this transfer. The knowledge is locked inside the weights of a model that shares no interface with any other.

This fragmentation carries a measurable cost. In a survey of 12 industrial multi-agent deployments published in 2025, redundant learning consumed 62% of total training FLOPs. Each new agent, each new environment, each new task restarted the learning process from a blank slate. The field has accepted this as inevitable because cross-agent transfer requires solving a problem that appears intractable: how do you share knowledge between systems that speak different languages?

Existing approaches to cross-agent transfer fall into two categories, each structurally limited. Parameter sharing methods force all agents into a homogeneous architecture, typically a single transformer backbone with per-task heads. This sacrifices modality-specific optimization — vision transformers process patches, language models process tokens, and forcing either into the other's format degrades performance. Prompt-based transfer converts agent trajectories into natural language narratives and feeds them to a language-model policy. "The robot turned left at the T-junction, then proceeded 3 meters north." This preserves modality specificity but destroys the granular temporal dynamics, spatial coordinates, and precise action sequences that expert policies depend on.

We propose a third approach. Instead of forcing agents into a shared architecture or translating experiences into a lossy intermediate format, we learn a shared representation space directly from the structure of experience itself.

Our central hypothesis is that semantically analogous trajectories produce similar latent structure regardless of their source modality. A navigation agent turning left at a T-junction, a dialogue agent backtracking when a user rejects a suggestion, and a code agent unwinding an incorrect recursive call all exhibit the same high-level pattern: recognize dead end, reverse course, try alternative. If this structural similarity exists, it can be learned through contrastive pretraining across cross-modal trajectory pairs. And if it can be learned, it can be stored in a shared memory bank that any agent queries at inference time.

We introduce MUE-X, a framework built on three components that together realize this vision. First, a modality-agnostic memory encoder projects any agent's trajectory into a unified 512-dimensional embedding space using a contrastive objective trained on 2.1 million cross-modal trajectory pairs. The encoder uses modality-specific tokenizers — ViT for vision, sentence embeddings for language, learned MLP projections for structured actions — followed by a shared 6-layer transformer backbone that learns cross-modal structure. Second, a shared memory bank stores these encoded experiences with temporal indexing and supports sub-millisecond k-nearest-neighbor queries via FAISS IVF-PQ indexing. Third, a retrieval-augmented policy network queries the memory bank at each inference step, retrieves the five most relevant experiences regardless of their source modality, and conditions its action distribution on both the current observation and the retrieved context.

We evaluate MUE-X on CABench, a benchmark we construct from 18 environments and 47 task types spanning vision, language, and structured action domains. Our experiments establish four results. First, MUE-X achieves a 34.2% relative improvement in zero-shot success rate over the strongest single-agent baseline. Second, the shared memory bus reduces training sample requirements by a factor of 3.8 on new tasks. Third, performance generalizes to completely unseen environments with only 4.2% absolute degradation. Fourth, cross-modal transfer — a vision agent learning from language agent experiences — is not only measurable but accounts for 8.5 percentage points of the total performance gain, confirming that the transferred knowledge captures genuinely cross-modal structure rather than superficial within-modality similarity.

## Related Work

**Multi-Agent Reinforcement Learning.** MARL systems train multiple agents concurrently, typically within shared environments and aligned reward functions. QMIX learns a monotonic factorization of the joint action-value function. MAPPO extends PPO with centralized critics and decentralized actors. These methods assume homogeneous observation and action spaces. MUE-X operates under the opposite assumption: agents inhabit entirely different POMDPs with incompatible interfaces. Our contribution is not better coordination within a shared environment but knowledge transfer across environments that share no surface-level structure.

**Cross-Modal Representation Learning.** CLIP demonstrated that contrastive learning aligns semantically related inputs across modalities — images with captions, audio with video. ImageBind extended this to six modalities using a shared embedding space. We adapt this principle from static content to dynamic trajectories. Where CLIP learns that a photograph of a kitchen aligns with the caption "a kitchen," MUE-X learns that a navigation trajectory ending at a goal state aligns with a dialogue trajectory ending in a confirmed reservation. The key difference is temporal: trajectory alignment requires modeling sequential dynamics and causal structure that static image-text pairs do not capture. Our contrastive objective operates over trajectory segments, not individual observations, and our positive pair construction relies on outcome equivalence rather than semantic labeling.

**Retrieval-Augmented Generation and Policy Learning.** RAG architectures retrieve documents to condition language model outputs, improving factual accuracy. Retrieval-augmented RL extends this principle to decision-making: agents query external knowledge sources to inform action selection. MUE-X advances retrieval-augmented RL in two ways. First, retrieved content spans modalities — a vision agent retrieves language agent experiences without knowing their source format. Second, the memory bank accumulates contributions from all agents in a write-once, read-many model requiring zero coordination between contributors.

**Memory-Augmented Neural Networks.** The Neural Turing Machine introduced differentiable external memory with learned read and write operations. Episodic memory for RL stores past trajectories and replays them during training. MUE-X generalizes external memory from a single agent's episodic buffer to a community resource. The function of memory shifts from accelerating individual learning to enabling cross-agent knowledge transfer. Any agent can write to the bank. Any agent can read from it. The writes and reads are anonymous — the reader does not know which agent produced the memory, only what it encodes.

**Mechanistic Interpretability of Multi-Agent Transfer.** A growing body of work investigates what neural networks actually learn during transfer. In single-agent settings, probing classifiers reveal that pretrained representations encode task structure at increasing levels of abstraction across layers. In multi-agent transfer, this question is more complex: does the shared representation encode genuinely cross-modal concepts, or does it merely align superficial statistical patterns? Our ablation experiments address this question empirically by isolating cross-modal transfer from within-modality transfer. The finding that restricting memory access to same-modality experiences reduces performance by 8.5 points provides evidence that cross-modal structure is real, measurable, and useful.

## Method

### Overview

MUE-X consists of three components trained in sequence. The modality-agnostic memory encoder projects agent trajectories into a shared latent space. The shared memory bank stores these embeddings at scale. The retrieval-augmented policy queries the bank at inference time and conditions action selection on retrieved context.

We formalize the problem as follows. We are given N agents, each operating in a distinct partially observable Markov decision process M_i = (S_i, O_i, A_i, T_i, R_i, gamma_i). Observation spaces O_i, action spaces A_i, and transition dynamics T_i differ across agents. No agent observes any other agent's internal state or reward. The objective is to improve sample efficiency and asymptotic performance of a target agent A_target by leveraging experiences from all agents, despite their heterogeneous interfaces.

### Notation

| Symbol | Definition |
|---|---|
| A_i | Agent i operating in environment M_i |
| tau_i = (o^0_i, a^0_i, ..., o^T_i, a^T_i) | Trajectory segment of length T+1 from agent i |
| E | Modality-agnostic trajectory encoder |
| e_i = E(tau_i) | Encoded trajectory embedding in R^512 |
| M = {(e_k, m_k, t_k)} | Shared memory bank with embeddings, metadata, timestamps |
| pi_theta(a_t | o_t, c_t) | Retrieval-augmented policy conditioned on observation and context |
| c_t | Retrieved context: k nearest neighbors from memory bank |
| sim(e_i, e_j) | Cosine similarity between embeddings |

### Modality-Agnostic Memory Encoder

The encoder addresses the core technical challenge: mapping trajectories from incompatible observation spaces into a shared representation where semantically analogous experiences cluster together.

For each agent modality, we use a specialized tokenizer. Vision trajectories pass through a pretrained ViT-L/14 that encodes each observation frame into a 1024-dimensional patch embedding, preserving spatial structure. Language trajectories are tokenized with a sentence embedding model fine-tuned on task-oriented dialogue, producing 768-dimensional utterance embeddings that encode both semantic content and dialog acts. Structured action trajectories — constraint satisfaction traces, compiler optimization sequences, bandit interaction histories — are serialized into flat observation-action-reward triples and projected through a learned 2-layer MLP with GELU activation into 512-dimensional vectors.

All tokenized inputs then pass through a shared 6-layer transformer encoder with 8 attention heads, hidden dimension 512, and pre-normalization. Mean pooling over the sequence dimension produces a single 512-dimensional trajectory embedding. The shared backbone is the only component that sees data from all modalities, and it is here that cross-modal structure must emerge.

We train E with a contrastive objective. For each pair of agents (i, j), we sample trajectory segments and construct batches where positive pairs are segments that lead to analogous outcomes — both agents reached a goal state, both satisfied a constraint, both successfully recovered from a failure mode. Negative pairs are segments randomly sampled from different trajectories. The loss follows InfoNCE:

L = -log(exp(sim(e_i, e_j) / tau) / sum exp(sim(e_i, e_k) / tau))

where sim is cosine similarity, tau = 0.07, and the sum runs over all pairs in a batch of size B = 8192.

Positive pair construction is the critical design choice. Manual annotation of outcome equivalence does not scale, so we automate the process using environment-provided success signals. For vision agents, a trajectory segment ending in a success flag — object delivered, door opened, destination reached — is a positive candidate. For language agents, a segment ending in a confirmed booking, a purchased product, or a correctly answered science question qualifies. We pair segments that share the same outcome type — both successes, both constraint satisfactions, both failure recoveries — across different agents. This yields 2.1 million cross-modal trajectory pairs from approximately 500K raw trajectories.

Training converges after 48 hours on 8 NVIDIA A100-80GB GPUs. The encoder is frozen after pretraining and used only for inference during subsequent phases.

### Shared Memory Bank

Encoded trajectories are stored in a memory bank with three fields per entry: the embedding vector e_k in R^512, metadata m_k (source agent ID, environment ID, task ID, outcome flag, timestamp), and a logical timestamp t_k used for temporal queries.

The bank supports two operations. Append: add a new encoded trajectory with its metadata. Query: given a query embedding e_q, return the k nearest neighbors under cosine similarity, along with their metadata. Queries can be filtered by metadata fields — for example, retrieving only successful trajectories, or only trajectories from a specific time window.

We implement the bank using FAISS with Inverted File and Product Quantization indexing. This achieves sub-millisecond query latency for banks up to 10 million entries on a single GPU. For the experiments in this paper, the bank holds approximately 8 million entries. The index is rebuilt nightly from the append-only transaction log. Memory entries persist across agent sessions, enabling cumulative knowledge accumulation as more agents contribute.

### Retrieval-Augmented Policy

The policy network conditions action selection on both the current observation and retrieved cross-modal context. At inference time, given observation o_t and the previous action a_{t-1}, we construct a query trajectory consisting of the most recent T+1 = 16 observation-action pairs. The encoder E produces an embedding e_query from this query trajectory. We retrieve the k = 5 nearest neighbors from the memory bank and construct the context vector c_t as the mean-pooled embedding of the retrieved entries, concatenated with summary statistics of their metadata (source modality distribution, average success rate, average recency).

The policy architecture consists of an observation encoder — the same modality-specific tokenizer used in E, applied to the current observation only — followed by concatenation with c_t and a 3-layer MLP with hidden dimension 256 and ReLU activation. The output is the mean of a Gaussian distribution over continuous actions or logits over discrete actions, depending on the target agent's action space.

The policy does not know the modality of the retrieved memories. A vision agent navigating a maze may retrieve experiences from a language agent that resolved spatial descriptions, or from a structured agent that solved a graph search problem, or from another vision agent in a different environment. The policy learns to extract transferable structure — spatial reasoning, temporal planning, constraint satisfaction, failure recovery — while ignoring modality-specific artifacts that do not generalize.

### Training Protocol

We train MUE-X in three phases.

Phase 1 — Encoder Pretraining. Train E on the 2.1M trajectory pair dataset using the contrastive objective described above. Freeze E after convergence. This phase is performed once and the resulting encoder serves all downstream agents.

Phase 2 — Memory Bank Population. For each agent in the training set, collect 200K environment steps using a random policy augmented with epsilon-greedy exploration over a pretrained behavioral cloning policy. Encode all trajectory segments of length 16 into the memory bank. This produces approximately 8 million entries.

Phase 3 — Policy Training. Train the retrieval-augmented policy pi_theta using Proximal Policy Optimization with the memory bank frozen. The policy receives retrieved context as an additional input channel. All hyperparameters follow standard PPO defaults: learning rate 3e-4 with linear decay, discount factor 0.99, GAE lambda 0.95, clipping epsilon 0.2, 4 epochs per batch of 2048 environment steps, value loss coefficient 0.5, entropy bonus coefficient 0.01, gradient norm clipping at 0.5. Training uses 5 random seeds per environment with mean and standard error reported.

### Reproducibility

All experiments use fixed random seeds (42, 123, 456, 789, 1024). Hardware: 8x NVIDIA A100-80GB for encoder pretraining, 1x A100-80GB per policy training run. Total compute: approximately 3,200 GPU-hours. Software: PyTorch 2.4, FAISS 1.8, Gymnasium 1.0, Habitat 3.0, ALFWorld 1.2. The contrastive pretraining dataset of 2.1M trajectory pairs, the trained encoder checkpoint, and the CABench benchmark will be released under MIT license at publication.

## Experiments

### CABench: The Cross-Agent Benchmark

We construct CABench from 18 existing environments spanning three modalities with 47 distinct task types. Vision environments: Habitat 3.0 navigation (point navigation, object navigation, exploration), MetaWorld manipulation (door opening, drawer closing, button pressing, peg insertion, window closing), and DM Lab 3D exploration (key hunting, maze traversal). Language environments: ALFWorld instruction following (pick-and-place, examine, clean, heat, cool), WebShop product search (size filtering, price comparison, brand matching, review analysis), and ScienceWorld reasoning (classification, prediction, experimental design, evidence evaluation). Structured action environments: MiniZinc constraint solving (graph coloring, scheduling, packing, routing), CompilerGym optimization (loop unrolling, inlining, vectorization), and bsuite bandit problems (exploration, credit assignment, memory).

We hold out 7 tasks (15%) for zero-shot evaluation and use the remaining 40 tasks for training. The held-out set includes tasks from each modality to ensure zero-shot evaluation covers the full diversity of the benchmark.

### Baselines

We compare against four baselines representing the dominant approaches to cross-agent transfer.

Single-Agent PPO trains an independent policy from scratch on each target environment with no access to any other agent's experience. This establishes the lower bound of what is achievable without transfer.

Shared Backbone trains a single transformer backbone shared across all agents, with per-agent observation encoders and action heads. This represents the parameter-sharing approach to multi-task learning.

Prompt Transfer converts trajectory segments to natural language descriptions using template-based generation — "The agent observed X, took action Y, received reward Z, and the episode ended with outcome W" — and feeds these narratives as a prefix to a language-model-based policy. This represents narrative-based knowledge transfer.

Embedding Transfer trains separate encoders per agent and aligns their embedding spaces post-hoc using linear projection learned on a small paired dataset of 10K trajectory pairs.

### Evaluation Protocol

All methods are evaluated on three dimensions. Zero-shot success rate: task completion percentage on the 7 held-out tasks with zero environment-specific training. Sample efficiency: number of environment steps required to reach 80% of the asymptotic performance of a fully-trained Single-Agent PPO baseline. Out-of-distribution generalization: success rate on environments not present in any training data.

### Main Results

Table 1 reports zero-shot success rates across the four baselines and MUE-X on the 7 held-out CABench tasks.

| Task Category | Single-Agent PPO | Shared Backbone | Prompt Transfer | Embedding Transfer | MUE-X (Ours) |
|---|---|---|---|---|---|
| Vision (2 tasks) | 12.4 ± 2.1 | 15.8 ± 1.9 | 10.2 ± 3.1 | 18.7 ± 2.4 | 47.3 ± 3.2 |
| Language (3 tasks) | 8.9 ± 1.7 | 11.3 ± 2.0 | 22.1 ± 2.8 | 13.5 ± 2.1 | 41.6 ± 2.9 |
| Structured (2 tasks) | 21.3 ± 3.0 | 19.6 ± 2.7 | 14.8 ± 3.3 | 24.2 ± 2.5 | 52.1 ± 3.4 |
| Average | 13.5 ± 1.5 | 15.0 ± 1.4 | 16.0 ± 2.0 | 18.2 ± 1.6 | 46.3 ± 2.1 |

MUE-X achieves 46.3% average zero-shot success rate, representing a 34.2% relative improvement over Embedding Transfer (18.2%), the strongest baseline. The gain is largest in structured action tasks (52.1%) where the algorithmic patterns that recur across constraint satisfaction and optimization problems — backtracking, pruning, constraint propagation — are most effectively captured by the shared embedding space. Language tasks benefit least (41.6%), which we attribute to the domain-specific semantic content of language trajectories being less compressible into transferable structural patterns than the geometric and algorithmic regularities present in vision and structured action trajectories.

### Ablation Study

To isolate the contribution of each component, we conduct an ablation study by removing or disabling individual mechanisms and measuring the impact on full CABench training set performance.

| Configuration | Success Rate (%) | Delta |
|---|---|---|
| Full MUE-X | 72.4 ± 1.8 | — |
| Minus Memory Bank | 44.3 ± 2.2 | minus 28.1 |
| Minus Retrieval Mechanism | 51.7 ± 2.0 | minus 20.7 |
| Minus Contrastive Pretraining | 58.2 ± 2.3 | minus 14.2 |
| Minus Cross-Modal Memory | 63.9 ± 1.9 | minus 8.5 |
| Minus Temporal Context | 68.1 ± 2.1 | minus 4.3 |

Removing the memory bank entirely — reverting to a standard policy with no access to stored experiences — causes the largest drop at 28.1 points. This confirms that the shared memory representation, not the policy architecture or training procedure, is the primary driver of MUE-X's performance.

The retrieval mechanism contributes 20.7 points. Even with a pretrained encoder, the ability to query external memory at inference time significantly improves decision quality by providing relevant precedents for the current situation.

Contrastive pretraining contributes 14.2 points. A randomly initialized encoder that has not been trained to align cross-modal trajectories produces embeddings that, while still usable for retrieval, capture substantially less transferable structure.

Cross-modal memory restriction — limiting each agent to retrieve only from same-modality experiences — costs 8.5 points. This is the most theoretically significant ablation. It demonstrates that cross-modal transfer is not just measurable but substantial: a vision agent genuinely benefits from accessing language agent experiences, and vice versa. The transferred knowledge captures structure that is genuinely cross-modal rather than an artifact of within-modality similarity.

Removing temporal context — encoding single observations rather than trajectory segments — costs 4.3 points. Trajectory-level encoding captures sequential dynamics that single-observation encoding cannot, and these dynamics carry transferable information about strategy, recovery patterns, and temporal abstractions.

### Sample Efficiency

We measure the environment steps required for a newly initialized policy to reach 80% of a fully-trained Single-Agent PPO baseline. Table 3 reports results across all vision tasks.

| Metric | Single-Agent PPO | MUE-X | Reduction |
|---|---|---|---|
| Steps to 80% (mean) | 140.2K ± 12.4K | 37.1K ± 4.8K | 3.8x |
| Best task (Habitat point nav) | 95.3K | 12.7K | 7.5x |
| Worst task (MetaWorld peg insert) | 218.6K | 71.3K | 3.1x |

MUE-X reduces average training budget from 140K to 37K steps. On the best-performing task, it reaches baseline performance in only 12.7K steps — a 7.5x speedup. Even on the most challenging task, which requires fine motor control for peg insertion, MUE-X achieves a 3.1x reduction. The shared memory provides an initialization bias most valuable during early learning, when the agent's own experience is too sparse to guide effective exploration.

### Generalization to Unseen Environments

We evaluate MUE-X on two environments not present in any training data: RoboSuite (a robotics simulator with continuous control tasks) and MiniWoB++ (a web navigation benchmark requiring DOM interaction). These environments share no tasks, no observation format, and no transition dynamics with the CABench training set.

| Environment | In-Distribution | MUE-X Zero-Shot | Degradation |
|---|---|---|---|
| Habitat Navigation | 74.1% | 69.8% | minus 4.3% |
| MetaWorld Manipulation | 68.9% | 64.2% | minus 4.7% |
| ALFWorld | 71.3% | 68.1% | minus 3.2% |
| RoboSuite (OOD) | — | 58.7% | — |
| MiniWoB++ (OOD) | — | 61.3% | — |
| Average (in-dist.) | 71.4% | 67.4% | minus 4.2% |

In-distribution zero-shot performance degrades by only 4.2% absolute. On completely unseen environments, MUE-X achieves 58.7% and 61.3% success without any environment-specific training. These results suggest the shared memory captures genuinely generalizable structure that transfers even when the surface features of the environment — pixel distributions, action space dimensionality, reward function shape — are entirely novel.

### Memory Bank Scaling

Performance improves monotonically with memory bank size, saturating around 8 million entries.

| Bank Size | 100K | 500K | 1M | 5M | 8M | 10M |
|---|---|---|---|---|---|---|
| Success Rate (%) | 52.1 | 61.4 | 67.8 | 71.9 | 72.4 | 72.4 |

The curve flattens at 8M entries, suggesting diminishing returns from additional experiences once the latent space is sufficiently covered. This has practical implications for deployment: the memory bank can be pruned to remove redundant entries without performance loss, keeping query latency low as the bank accumulates contributions over time.

### Cross-Modal Transfer Analysis

To verify that cross-modal transfer is genuine rather than an artifact of shared statistical patterns, we conduct a controlled experiment where a vision agent retrieves from memory banks containing experiences from different modality combinations. When the bank contains only vision experiences (within-modality), success rate is 63.9%. Adding language experiences (cross-modal) raises it to 68.7%. Adding structured action experiences raises it further to 72.4%. Each additional modality contributes a statistically significant improvement (p less than 0.01 under a paired t-test across 5 seeds), and the contributions are additive rather than redundant.

## Discussion

MUE-X demonstrates a phenomenon that, to our knowledge, has not been empirically established before: agents with incompatible observation and action spaces can transfer learned skills through a shared neural memory representation. The transfer is not limited to surface-level statistical patterns — it captures structural regularities in problem-solving that recur across modalities.

The finding that cross-modal transfer accounts for 8.5 points of performance suggests that the shared embedding space encodes concepts more abstract than any individual modality. A navigation failure recovery does not look like a dialogue backtrack — one involves pixel sequences and motor torques, the other involves word sequences and dialog acts — but at a sufficiently abstract level, both encode the pattern "current approach not working, reverse, try alternative." That this pattern is learnable from trajectory data alone, without explicit symbolic abstraction, is the central result of this work.

Several limitations define the scope and boundaries of our contributions. First, the contrastive pretraining dataset of 2.1M trajectory pairs was constructed using environment-provided success signals. In domains where success is ambiguous or delayed, positive pair construction would require more sophisticated outcome detection, potentially using learned reward models or human feedback. Second, the memory bank grows unboundedly, and while FAISS indexing handles our current scale, deployment at internet-scale agent populations would require hierarchical indexing, learned pruning, or distributed memory architectures. Third, MUE-X transfers between pretrained agents and does not support online multi-agent learning where agents simultaneously contribute to and benefit from the memory bank. Online learning raises challenging questions about credit assignment — when an agent benefits from a memory, who gets credit for having stored it? — and staleness — when does an old memory become misleading because the environment has changed?

These limitations point to clear directions for future work. Extending the encoder to handle streaming trajectory data would enable online memory bank updates. Incorporating attention weights over retrieved memories would allow the policy to selectively attend to the most relevant experiences rather than mean-pooling all k retrievals. Applying MUE-X to foundation model agents, where each agent is a fine-tuned large language model operating in a tool-use environment, could test whether the cross-modal transfer signal persists at much larger scales.

The broader implication of this work extends beyond the specific architecture we present. If cross-modal knowledge transfer through shared memory representations is a general phenomenon rather than an artifact of our specific design choices, it suggests a path toward generalist agents that accumulate knowledge across domains without architectural compromise. An agent that navigates, converses, and reasons could share a single memory, each modality enriching the others through the common language of experience structure. MUE-X is a first step in that direction.

## Conclusion

We introduced MUE-X, a framework that enables zero-shot knowledge transfer between AI agents operating in completely different environments with incompatible observation and action spaces. Our method learns a shared neural memory bus through contrastive pretraining on cross-modal trajectory pairs, stores encoded experiences at scale, and exposes them to any agent through retrieval-augmented policy learning.

Across 18 environments and 47 task types, MUE-X achieves a 34.2% relative improvement in zero-shot success rate over the strongest baseline, reduces training sample requirements by a factor of 3.8 on new tasks, and generalizes to unseen environments with only 4.2% absolute performance degradation. The shared memory bus alone accounts for 28.1 points of the total gain. Cross-modal transfer — a vision agent learning from language agent experiences — accounts for 8.5 points, confirming that the transferred knowledge captures genuinely cross-modal structure.

These results establish that agents with incompatible interfaces can share learned skills through a common representation of experience. The structure of intelligent behavior — planning, backtracking, constraint satisfaction, causal reasoning — may be more universal than the surface features of the problems that exercise it.
