# Piazza Post Scraper and Markov Chain Text Generator

Have you ever finished a weekly reading for a course and not known where to start with your Piazza post? Inspired by Andrey Markov’s work on generative modeling for natural language, we have developed an interactive tool that allows students to auto-generate Piazza posts for a given set of weekly readings. Our application, trained on data collected from Piazza posts for Dennis Tenen’s Literature in the Age of Artificial Intelligence (Spring 2020), uses a Markov Chain to generate a response to texts from each of the first 6 weeks of the course’s readings. Furthermore, students using the app have the option to rate the quality of a generated post. Our app is connected to a server, which tracks the average post score for all users who have used the app. By doing so, we conduct a sort of Turing test for the Markov Chain and are able to quantify how well it performs. The end result is a Graphical User Interface (GUI) which generates a new piazza post given a trained Markov Chain while tracking the live performance of the model for all users.


Steps to Scrape Your Own Piazza Discussion Board:<br>
  - fill in `username`, `password`, `courseID` in `config.py`<br>
  - call scraper and write text to a file<br>
To generate Text without GUI:<br>
  - call `fillDict()` on text file<br>
To generate Text with GUI:<br>
  - edit `text_generator` so generated texts prints out with a command line argument 
