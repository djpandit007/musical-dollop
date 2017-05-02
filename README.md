# musical-dollop
Adaptive Learning System using Action Language

This repository is the final project of the course CSE 579 - Knowledge Representation at Arizona State University. We are attempting to build an adaptive learning system using the BC+ action language. We are using cplus2asp for modeling our solution. Given a set of topics covered in a course and their dependencies, our system will plan a course-route to cover all the topics based on initial Knowledge of the learner.

In addition to this, we have also used Alchemy, which is a software package providing a series of alorithms for statistical relational learning and probabilistic logic inference, based on the Markov logic representation. Using Alchemy, we are estimating the topics the learner has mastered and the topics which need more work. We are currently doing this using [randomly generated dataset](https://www.random.org "Random.org's Homepage") however, the idea would still work on actual data from in-class quiz and/or midterm exam.

Cplus2ASP: http://reasoning.eas.asu.edu/cplus2asp/
Alchemy: https://alchemy.cs.washington.edu/
