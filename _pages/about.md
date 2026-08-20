---
layout: about
title: me
permalink: /
subtitle: >
    Research Scientist at Scale AI
    <!-- <p class="motto"> <em> motto </em> </p> -->
profile:
  align: center
  image: prof_pic.jpg
  image_circular: false # crops the image to make it circular
  address: >
    <p> akyurekafra [at] gmail [dot] com
    <p> San Francisco Bay Area </p>
news: true  # includes a list of news items
latest_posts: false  # includes a list of the newest posts
selected_papers: true # includes a list of papers marked as "selected={true}"
social: false  # includes social icons at the bottom of the page
---
I am a Research Scientist at [Scale AI](https://scale.com/), where I work on LLM post-training, evaluation, and human data programs.

On the evaluation side, I have led human data curation for [PRBench](https://labs.scale.com/papers/prbench) and [DrugDiscoveryBench](https://labs.scale.com/leaderboard/drugdiscoverybench). PRBench measures how well language models handle open-ended, high-stakes work in law and finance using expert-authored tasks and detailed rubrics. DrugDiscoveryBench evaluates agents on multi-step computational and information-retrieval tasks in early-stage drug discovery. More broadly, I have extensive experience designing human data programs for complex, economically valuable workflows, including synthetic-data pipelines for later-stage drug development tasks such as clinical study report authoring.

On the post-training side, I am especially interested in online learning, synthetic data, and self-supervision. In [RL4F](https://aclanthology.org/2023.acl-long.427/), we trained a critique model to generate natural-language feedback that helps a larger, fixed language model revise its outputs. [Deductive Closure Training (DCT)](https://aclanthology.org/2024.findings-acl.584/) uses model-generated implications and contradictions to improve factual coherence and make model knowledge easier to update. In [OnlineRubrics](https://labs.scale.com/papers/onlinerubrics), we developed a method that dynamically elicits evaluation criteria during reinforcement learning so that the reward can adapt as new model behaviors emerge.

More broadly, my research asks how language models can learn from feedback—whether expressed in natural language or gathered through interaction with their environment. Inspired by the way people revise their knowledge and beliefs in response to feedback, I am interested in methods that help models update their outputs in light of facts, requirements, natural phenomena, and human preferences. My goal is to build language models that incorporate such feedback consistently and become more reliable collaborators.

Before joining Scale, I completed my PhD in Computer Science at [Boston University](https://www.bu.edu/cs/), where I was advised by [Derry Wijaya](https://derrywijaya.github.io/web/). I also had the opportunity to collaborate with researchers at the [Allen Institute for AI](https://allenai.org/), [Apple](https://machinelearning.apple.com/), and MIT, including [Jacob Andreas](https://www.mit.edu/~jda/).



<!-- **Improving Language Models with Feedback**

How can we alter language models to adhere to natural language feedback?

<div class="about-highlight" markdown="1">
- We have devised an automatic [critique generator](https://arxiv.org/abs/2305.08844) called RL4F which is trained with reinforcement learning. RL4F is trained via reinforcement learning and rewarded as long as the generated critiques improved a second model's predictions.

- I have led the curation of a model editing benchmark [DUnE](https://arxiv.org/abs/2311.16087) where edits are natural language sentences. We also showed that retrieval augmented language modeling is superior to specialized editing techniques when edits are natural language phrases.

- Moreover, I have developed [a scheme](https://arxiv.org/abs/2110.07059) that enables growing the number of a classes that an object classifier can recognize using language information about the objects such as labels and descriptions.
</div> -->

<h2 style="margin-top: 1rem;">biography</h2>
{%- include_relative bio.md %}
