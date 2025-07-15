---
layout: post
title: How to write a living literature review
subtitle: Finding papers, coming up with ideas, writing and publishing
tags: [Further Reading, Meta]
comments: true
readtime: true
---

So, how do you actually write a living literature review? In the more than two years that I have been writing this (time really flies), sometimes I get asked how I go about writing the posts here. With this post, I want to answer this question. While this is focussed on a living literature review, I think these notes are probably helpful for everybody who has to do at least some scientific writing or wants to do more of that in the future. Also, at least the first two thirds of the post is exactly the same approach I use to write scientific papers. 

# Finding relevant literature

I think the most essential part of the process is finding relevant papers to read and write about. This is more difficult than you might think. If you are working in a highly specialized discipline, you can often just subscribe to your favorite topic on ArXiv and you are golden. However, once you start to do interdisciplinary work (which this living lit review clearly is) you run into the problem that there is no obvious place to look for papers. Over time, I have found some places that yield reasonable results, but if you are on your interdisciplinary journey, you just have to accept that your false positive rate will always be pretty high in the papers you look at. In the following, I will give a quick description on how you can find relevant literature. 

# Using good keywords

Before we dive into the different services you can use here, one meta point. When you are using many of these services, you have to define what kind of research you are looking for. Here you have to tread the fine line between too general and too specific. You have to find a keyword which is used in the research around the topic you are interested in, but it should not be so obscure that you have to set thousands of alerts to get a paper a week. On the other hand, if you use something like “climate change” as your keyword, you will be absolutely flooded with emails. An example of a keyword on the level of specificity that regularly provides results, but does not overwhelm me with alerts is “Global Food Trade”. Too broad would be “Global Trade” and too specific would be “Global Wheat Trade”. 

So far I have found two good ways to generate these goldilocks keywords:
* Feed a few papers to the LLM of your choice and ask it what good keywords would be if you were looking for similar research. 
* Search for papers you find interesting on [OpenAlex](https://openalex.org/) (more about OpenAlex below). Once you get the results of your query, you can add a keywords tab there. These are automatically generated keywords by OpenAlex, based on their own bibliometric analysis. These often capture the ideas you are looking for quite well and can be used to search for more. 

## [Google Scholar](https://scholar.google.com/) alerts

Google Scholar tries to index a large chunk of scientific literature. While it has some blind spots (like that it does not index [Zenodo](https://zenodo.org/)), it usually does a good job in finding papers. When you have a profile at Google Scholar, you can set alerts. This means you get an email every time a new paper is found by Google Scholar which mentions the keyword you specified. 

## [Research Gate](https://www.researchgate.net/)

Research Gate is a website for researchers to share their work and connect with other researchers. In the home tab of their website you are presented with papers that might be interesting to you. I have found that the algorithm often works reasonably well, it is just cumbersome to train. It is based on the papers you have uploaded, which people you follow and what papers and topics you have interacted with in the past. This means it takes some work to put in all this info and find interesting researchers to follow, but once this is done, it sometimes surfaces papers I do not find anywhere else.
 
## [OpenAlex](https://openalex.org/)

OpenAlex is a bibliographic catalogue of scientific papers. It is similar to other bibliographic catalogues like Web of Science, but it has the big advantage that it is completely free and available to everyone. You can search directly on their website, but they also have an API that lets you request papers. To make the usage easier, I wrote [some code](https://github.com/florianjehn/OpenAlex-Paper-Request) (thanks Claude) to query the API. This allows you to request papers about specific topics in a defined date range and you will get a nice csv file which you can browse through to check if you found interesting papers. 

## Newsletters of research orgs
Well, this one is pretty self-explanatory. Research orgs like to boast about the stuff they publish. So, find the newsletters of the research orgs you like and subscribe to it.

## [TERRA](https://www.cser.ac.uk/work/the-existential-risk-research-assessment-terra/) (unfortunately deprecated)

[CSER](https://www.cser.ac.uk/) did have a tool that tried to automatically find papers that are relevant to global catastrophic risk. Unfortunately, they recently discontinued it and you can only download the past results. Though, this still contains a lot of gems. 

## Going to conferences

Find big, interdisciplinary conferences and try to look at as many scientific posters as you possibly can. Obviously, the error rate is pretty high here, but this also gives you the most recent research and papers to look out for in the not too far future and you can easily look at several hundred posters in a few hours.

## Looking at the reference list 

Scientific papers reference other papers for their claims. If you found a claim interesting, just dig up the referenced paper. 

## Finding specific papers
Sometimes you already have a hunch of what kind of papers you are looking for, like when there is a gap in argument that would profit from a fitting citation. For this case, there are also a bunch of very helpful tools out there:
* [Elicit](https://elicit.com/): This is a search engine optimized for finding the papers you need and it can also automate information extraction. Just ask whatever interests you and it will try to find papers which answer your questions. It is kind of optimized for medical papers, but in my experience it can also be quite helpful for many other fields. 
* [Connected Papers](https://www.connectedpapers.com/): The main usage of this tool is to find the web of papers that surrounds a specific paper. You put in the name of a paper that you find interesting and you’ll get a network of papers relevant to it. These papers are selected based on similarity, which is calculated by checking if papers are overlapping in their citations and references. 
* [Research Rabbit](https://researchrabbitapp.com/): This is a bit of a mix between the other two tools. Allowing you to search in the network of papers you have specified.

# Reading and taking notes
Alright, now you have a big stack of papers you might be interested in, but you still have to read them. It can be tricky to find a set-up that allows you to comfortably read a lot of papers (at least it was for me). But by now I have a workflow that allows me to read papers easily and still be able to extract the information without too much overhead:

* Add the papers to [Zotero](https://www.zotero.org/): Zotero is a great, free tool to organize the things you want to read. It automatically gets you all the metadata for the paper and you can even add them directly from your browser. 
* Get the papers on your reading device: I am using a [Boox Note Air 2](https://euroshop.boox.com/collections/e-ink-tablets/products/noteair2promo?variant=42340358979784). I like these because they have an E-Ink display, but under the hood this is just a normal Android tablet, so all your normal apps work. But you can use any device you enjoy reading on, as long as it allows making notes. To get the papers on the tablet, I just have a folder on my computer that synchronizes with the tablet. To get the papers in the folder I use the [Attanger](https://github.com/MuiseDestiny/zotero-attanger) extension for Zotero. 
* Read and annotate the papers: On the Boox I can just underline everything in the paper I find interesting and scribble handwritten notes in the margins. Once I have finished a paper, I sync it back to my computer. I select the papers to read by the date they were added, so first in, first out. 
* Get the notes out of the paper: Zotero allows you to automatically extract everything you have underlined in a pdf, so I do just that. 
* Making your notes permanent: To make use of your notes, you have to find a permanent place for them, where they can be easily connected with other things you write. For this I use [Logseq](https://logseq.com/). In Logseq you can import papers directly from Zotero. Once you have done that, this creates a new page for your paper with all the underlined text being directly added. On this page I then order the notes and write down all my handwritten notes. I also add tags to find things more easily in the future. I also specifically tag all the papers that I think would make a good post and link them to other papers of that topic. Logseq allows you to query your notes. I use this feature to automatically create a list of all the post ideas I have written down anywhere in my notes. 

# Coming up with ideas

Once you have done all these steps to find, read and digest papers, I think you have already done the most important things you can do to come up with ideas to write about. Because in my experience the amount of ideas you have is very directly correlated with the amount of papers you read. This might seem obvious, but it wasn’t to me when I started to become a scientist (and nobody bothered to tell me). I think this is because in my experience many scientists just don’t read that much, so they never realize what they are missing. I started to move in the direction of reading more after I had finished my PhD, because I noticed that I did not have many good research ideas. On my journey to find out how to have better ideas, I came across the book “[Constructing Research Questions](https://www.goodreads.com/book/show/17323972-constructing-research-questions)” by Mats Alvesson and Jörgen Sandberg. I won’t go into much detail here, because I have already written a summary [here](https://florianjehn.github.io/Societal_Collapse/2023-02-03-gap_spotting/), but the main gist of the book is “You have to read more! If you think you are reading enough, read more! If you think you read too much, you don’t, read more instead.” And I think this is spot on. Because if you want to have good ideas, you have to know what others have already done, in what direction your field is developing, what techniques and methods are out there and what the big questions are that people are grappling with. The only way to get this information reliably is to read a shitload of papers. Pretty much all the good ideas I had I can attribute to just reading more and I think simply reading more is a skill that is underutilized by many scientists. All the posts in my living literature review started their life as notes scribbled on pdfs. Same goes for all the papers I have written since my PhD. 

# Writing a post

This is actually the easiest part, because you have already done all the hard work in the previous steps. The way I go about it is just to look at the automatically generated list of post ideas in Logseq and pick one that catches my interest on that day. Then I take a quick look at all the notes of the relevant papers and draft an outline of my argument. In many cases I can just use my previously made notes almost one to one. Once I have a first draft going, I usually send it to one of the people from whom I have summarized papers and ask for feedback. This results in a positive answer most of the time, because people like it when you are interested in their work and are happy to tell you where you might have misunderstood their argument or technique. As soon as I have incorporated the feedback, I put the post on a schedule to be published. 

# Technical setup

To distribute my posts, I have two separate systems. Github Pages for my permanent archive of posts and Substack for an easy way for people to subscribe to my work and also to get some more engagement via their algorithm. 

## Github Pages

I use Github Pages for making sure that I have an easy way to make my posts available for the long term and be able to track changes. Also the actual posts are just stored as markdown files, so if Github tries to do [enshittification](https://en.wikipedia.org/wiki/Enshittification), I can easily move somewhere else. 

### Get a Github account

Don’t think I have to explain that one.

### Set up your Github Pages with Beautiful Jekyll

[Beautiful Jekyll](https://beautifuljekyll.com/) is a template for easy to modify static websites. They have a good get started [guide](https://github.com/daattali/beautiful-jekyll#readme), but I’ll give an overview + some extras:
* Fork the Beautiful Jekyll repository and make sure to rename it to YOURUSERNAME.github.io This allows Github to understand that it is supposed to make a Github Page out of this. This will create a static website at https://YOURUSERNAME.github.io
* Set-up [Github Desktop](https://desktop.github.com/download/) on your computer. This program allows you to download from and upload to the repository you just created. Use it to clone your repository to a local folder of your choosing. Once you change anything in that folder Github Desktop will see this and allow you to upload the changes again to your online repository. Once they are uploaded, Github will build the website again with your changes. 
* In your local folder of your repository, you should find a file called **_config.yml**. This file lets you change pretty much everything on your website. Play around and find out. 

If you like [how I have set up things](https://florianjehn.github.io/Societal_Collapse/), you can also just do these steps, but fork my repository instead of Beautiful Jekyll. 

### Publishing posts
Your repository should contain a folder called posts. In this folder you can put markdown files with the following naming system **YYYY-MM-DD-name_of_your_file.md**. When you upload this file to your repository using Github Desktop, Github will create a new post on the date you have specified in the name. If the date is in the past, it will create the post immediately. See [here](https://raw.githubusercontent.com/florianjehn/Societal_Collapse/refs/heads/main/_posts/2020-10-28-bronze_age.md) for an example of how these files are formatted in markdown. 

## Substack

Setting up a Substack is pretty self-explanatory and there are many tutorials out there, so I won’t go into detail here. But what I found to be most helpful to get a wider readership was recommendations from other substacks. To get them, just talk to people that write about similar things as you do and convince them that your work is relevant to their readers as well. 

## Making everything citable

As this blog is essentially just another form of doing research, I wanted to make sure that my blog is both findable via academic channels and also that the people I cite can become aware of what I am doing here. This seemed quite difficult to accomplish, until I came across [Rogue Scholar](https://rogue-scholar.org/), which aims to be a home for scientific blogs. It is a platform which automatically creates DOIs for my blog posts, as well as extracting the references I have, so other people can see that I cited them.

To also set this up for your living literature review you have to go through a few steps:
* Create an account at Rogue Scholar (optional).
* Fill out the [blog questionnaire](https://tally.so/r/nPvNK0). This gives Rogue Scholar the information it needs to figure out if your work is actually a scientific blog.
* Wait a day or so. 
* Once Rogue Scholar has decided that your work is a scientific blog, they will go through all your existing posts to archive them and provide them with DOIs. The end result will look something like [this](https://rogue-scholar.org/communities/existentialcrunch/records?q=&l=list&p=1&s=10&sort=newest). 

Every time you add a new post on your blog, this will also be added to the archive. The DOI forwards you to the original blogpost, unless this is not available anymore, in which case it falls back to an archived version in the [Internet Archive](https://archive.org/).

When I have updated posts, I have to inform Rogue Scholar manually, as Substack does not automatically provide this information (Wordpress for example does). Rogue Scholar will then update the version on their end as well.

You can also add additional meta data like your [ORCID](https://orcid.org/0000-0002-7296-8008) or funding information, if you want to. 

Overall, it is a pretty cool solution! And now every post of mine also has a “How to cite” section. 


# Promoting your work

This is my least favorite part of the whole endeavour, so I might be doing this suboptimally. But by now I have several channels where I notify people when I have written something new. I will write a short summary of my new post and why I think it might interest people. I then publish this summary, together with a picture from the post and a link to it on LinkedIn, Substack Notes and Mastodon (with a bridge to Bluesky). I also send out an email to all the subscribers of my newsletter. The vast majority of readers come via the email newsletter, but there is enough readership from all the other channels to justify doing the extra work there. 

# How to start your own living literature review?

Congratulations, you now know how to do your own living literature review. If this got you interested in writing one, you can. Open Phil is still looking for people who want to try out this way of scientific writing. You can find me info [here](https://mattsclancy.substack.com/p/time-for-more-living-literature-reviews). 

# How to cite
Jehn, F. U. (2025, April 23). How to write a living literature review. Existential Crunch. [https://doi.org/10.59350/2vd97-whc20](https://doi.org/10.59350/2vd97-whc20)

