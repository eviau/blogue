Quitting data science
=====================

.. post:: Aug 13, 2022
   :tags: data-science
   :author: me
   :language: en

This is a rough draft explaining my thought process about data science after having worked briefly in the field a few years ago.

a data science hiatus
---------------------

Maybe data science is simply not for me. Maybe we are not doing data
science the way it should be done. Maybe it’s not possible to do data
science the way we need it to be done. In any case, here is why I am
currently refraining from doing more data science work.

my background
~~~~~~~~~~~~~

mathematics, finance, arts, philosophy, programming

what business want from data science
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most businesses I have observed want a more predictable world in which
to conduct their business. They want to have actionable results on which
to build their enterprise. Sometimes data science can deliver these
actionable insights, sometimes it cannot. Often, these results start by
wanting to know something, or confirming that we do know that thing we
think we know. Let’s look at this in a matrix of before data science and
after data science:

.. list-table:: before/after DS

	* - before/after DS
	  - we can know
	  - we cannot know
	
	* - we think we know
	  - confirmation (useless) / infirmation (useful)
	  - "we obviously know this, how can you not tell us more???"
	  
	* - we think we do not know
	  - Magic! Wonderful!
	  - "why did we hire you again?"

Let’s go through this table together.

If the business thought they knew something and wanted a confirmation of
it, two things are possible:

-  the knowledge is confirmed: then you are useless because we already
   knew that thing, why did we need confirmation ? This is often not
   considered actionable insight because it is not a hidden insight.
-  the knowledge is infirmed: now this is an insight, but the game
   becomes a status game - how do you communicate your results in a way
   that is helpful to those who need them without stepping on anyone’s
   toes ?

If the business thinks they know something and you tell them you cannot
possibly devise a way of confirming/infirming the knowledge, then you
have to explain how it is impossible to know this, since they obviously
know this fact ! You are then also near useless.

If the business thinks they do not know something they need to know, and
you are able to tell them, then you have worked your data science magic
and your job is justified… but you also have raised the stakes for
yourself and now need to do more of this more often.

If the business thinks they don’t know something and you cannot tell
them anything to help them, congrats! you are useless.

So data science is half hard work, half communication work bordering on
the political.

The epistemological status of data science
------------------------------------------

I often feel that data science is based on believing that it is possible
to know everything about anything, given that we have enough data.

I am no physicist, but my understanding of things like the `uncertainty
principle <https://www.feynmanlectures.caltech.edu/I_37.html>`__ lets me
know that this is not the case.

Another option is in psychology, we have the `observer
effect <https://en.wikipedia.org/wiki/Observer_effect>`__.

Some things change as soon as we observe them, and this impacts the
data. There are things we could not know even if we had all the data in
the world.

A simple example of this would be asking someone who looks sad or angry
if they are doing well; they might respond that it was fine up until you
asked them, and now they realize that they are not doing so well.

I wrote `a short story of fiction on the effects of believing in
determinism as a general guiding
principle <https://finartcialist.com/fr/oeuvres/ilfautqueturuinestout.html>`__.

what it means to know something: data and models
------------------------------------------------

How do we know that the sun will rise tomorrow ? We know it because we
have data - we have seen it happen in the past - and a model - we
devised an abstraction of the real world that makes sense given the data
and enables us to predict what is going to happen in the future.

I would argue that there are different kinds of models - a machine
learning model, often used in data science, does not have the same
epistemological status as the model used to say that the sun is at the
center. And that these different kinds of models allow for different
kinds of knowledge. It is important not to confuse these different
kinds, to not be mistaken by their name.

There are probably more than these two types, but let’s start with the
machine learning model and the physical model.

In the machine learning model, let’s say a computer vision model where I
am trying to identify images - the knowledge I am experimenting on is on
image identification, but the knowledge we would like to gain is
insights on how we learn. It’s a model about learning, not about
computer vision. The computer vision task is only an experiment, one
data point, in trying to figure out how we learn.

In the physical model, let’s say we re-use the sun at the center of the
solar system one - the knowledge I am experimenting on is on the
localisation of planets in some sort of space, which is also the
knowledge we would like to gain. The model is the learning, and the data
about the sun rising everyday is one experiment to test this model.

How do we know that we have the right model ? We look at the data, we do
experiments. This stands for both.

But what happens when the model is not also the expected learning ?

For me the big difference is in how we can **iterate**. In machine
learning experiments, we iterate by changing models architecture, but we
also iterate by training our model on test data. Which one should be
considered the scientific experiment here, I am not sure…

What’s lacking for me are two things: change of paradigm (from Kuhn) and
falsifiability (Popper). It’s strange to put them together on the same
task, probably a misunderstanding on my part - but let me explain my
thoughts.

Change of paradigm for the physical model would be to say, this planet
is not here - this planet is actually here. Or this planet follows this
path along the sun, not this one. Or - what have happened historically -
the sun is at the center, not the Earth. The question we are asking is
“maybe this is not how it works”.

Change of paradigm for the machine learning model would be to say, this
is not how we learn. This is what we are trying to model after all - how
we learn, how we can make computers learn in similar or different ways.
Change of paradigm is about the thing which we want to learn about, not
about tweaking experiments.

Falsifiability, for the physical model, to find one counter-example -
one day where the sun does not rise - to help up dismiss an idea.

Falsifiability, for the machine learning model… I am not sure how it
would look like. And this is a real question that I have because I think
that this is where everything changes. What is the counter-example to
this model cannot learn ? You need to find one thing it cannot learn.
But to show that the model cannot learn this specific thing you need to
run a possibly infinite amount of experiments where it fails to learn
that thing. Are there other ways ?

a few years later...
--------------------

I am going to publish this as is.

I have started to read some books, like `Knowledge and its limits <https://en.wikipedia.org/wiki/Knowledge_and_Its_Limits>`__ and I feel like I will have more to say in the future. We will see.


