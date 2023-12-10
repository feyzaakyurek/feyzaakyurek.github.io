---
layout: about
title: me
permalink: /
subtitle: >
    PhD Student in Computer Science at Boston University
    <!-- <p class="motto"> <em> motto </em> </p> -->
profile:
  align: center
  image: prof_pic.jpg
  image_circular: false # crops the image to make it circular
  address: >
    <p> akyurek [at] bu [dot] edu
    <p> 665 Comm Ave, Boston, MA </p>
news: true  # includes a list of news items
latest_posts: false  # includes a list of the newest posts
selected_papers: true # includes a list of papers marked as "selected={true}"
social: false  # includes social icons at the bottom of the page
---
I am a fifth-year Computer Science PhD student at Boston University focusing on natural language processing.

My research focuses on enhancing language model interactions to be more akin to human-like communication. Having inspired by how humans modify their knowledge and beliefs through feedback received in natural language, my specific interest lies in how such feedback, expressed in natural language, can *guide a language model’s outputs to align with facts, requirements, natural phenomena, or preferences*. My aim is to develop methods that enable language models to incorporate this feedback consistently, thereby enhancing their alignment, reliability, and safety.

I have the privilege of being guided by [Derry Wijaya](https://derrywijaya.github.io/web/). Recently, I had the enriching experience of collaborating with the talented teams at [Allen AI](https://allenai.org/), [Apple](https://machinelearning.apple.com/) and I often collaborate with [Jacob Andreas](https://www.mit.edu/~jda/) at MIT.


<p style="text-align: center;">I am currently exploring opportunities in the industry job market!</p>



**Improving Language Models with Feedback**

How can we alter language models to adhere to natural language feedback?

<div class="about-highlight" markdown="1">
- We have devised an automatic [critique generator](https://arxiv.org/abs/2305.08844) called RL4F which is trained with reinforcement learning. RL4F is trained via reinforcement learning and rewarded as long as the generated critiques improved a second model's predictions.

- I have led the curation of a model editing benchmark [DUnE](https://arxiv.org/abs/2311.16087) where edits are natural language sentences. We also showed that retrieval augmented language modeling is superior to specialized editing techniques when edits are natural language phrases.

- Moreover, I have developed [a scheme](https://arxiv.org/abs/2110.07059) that enables growing the number of a classes that an object classifier can recognize using language information about the objects such as labels and descriptions.
</div>

<p></p>
**Safety in Language Models**

How to make language models safer with language feedback?

<div class="about-highlight" markdown="1">
- I have studied [bias measurement](https://arxiv.org/abs/2205.11605) in instruction-tuned language models and conducted sensitivity [analysis](https://arxiv.org/abs/2205.11601) for measuring bias in language models.

- A significant portion of our model editing benchmark DUnE includes edits that solicit debiased model outputs. We [find](https://arxiv.org/abs/2311.16087) that language models struggle parsing the instructions that call for avoiding harmful biases and stereotypes.
</div>

<h2 style="margin-top: 1rem;">biography</h2>
{%- include_relative bio.md %}
