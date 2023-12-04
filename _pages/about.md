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

My research focuses on enhancing language model interactions to be more akin to human-like communication. This involves understanding how humans modify their knowledge and beliefs through feedback received in natural language. My specific interest lies in how such feedback, expressed in natural language, can *guide a model’s outputs to align with facts, requirements, natural phenomena, or preferences*. My aim is to develop methods that enable language models to incorporate this feedback consistently, thereby enhancing their alignment, consistency, and safety.

I have the privilege of being guided by [Derry Wijaya](https://derrywijaya.github.io/web/). I earned my Master's in Statistics from Carnegie Mellon University. Recently, I had the enriching experience of collaborating with the talented team at [Allen AI](https://allenai.org/), as detailed in our joint work [here](https://aclanthology.org/2023.acl-long.427/) and I often collaborate with [Jacob Andreas](https://www.mit.edu/~jda/) at MIT. **I am currently exploring opportunities in the industry job market!**


**Improving Language Models with Feedback & Model-Editing**

How can we alter language models to adhere to natural language feedback?

<div class="about-highlight" markdown="1">
- I have devised an automatic [critique generator](https://arxiv.org/abs/2305.08844) which is rewarded via reinforcement learning as its critiques improved another model's predictions.

- I am interested in aligning language models via natural language feedback, so I have led the curation of a model editing benchmark [DUnE](https://arxiv.org/abs/2311.16087) where edits are in natural language. We also showed that retrieval augmented language modeling is superior to specialized editing techniques when edits are natural language phrases.

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
