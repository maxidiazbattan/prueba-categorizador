# Categorizer for e-commerce

This project is about creating a categorizer, that is, designing a machine learning model so that based on certain features such as "id", "family, "group", etc., it categorizes the entire batch of products of a e-commerce of auto parts.

## Getting Started

The best way to run it without the need to install practically anything is to run it in google colab. The only thing you will need is to install streamlit. In a cell copy the code, and at first paste the magic method "%%writefile app.py", to run it in another cell paste the following statement, "!streamlit run app.py & npx localtunnel --port 8501". See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
!pip install streamlit -q
```

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

To test it just use the file test.csv

```
Drag and drop or browse the file into the ML app 
```

## Deployment

To do the deployment I have used a platform called Heroku, which is a cloud platform that lets companies and devs, build, deliver, monitor and scale apps, in a very simple way. For this case I made it super simple, you only need to connect your repo with Heroku, once it's connected, click on deploy branch. I'll leave you the app link to see the final result. 

app link: https://categorizerrepuestosya.herokuapp.com/
## Built With

* [Streamlit](https://streamlit.io/) - The web framework used
* [Heroku](https://devcenter.heroku.com/) -  Cloud deployment platform


## Author

* **Maximiliano Diaz Battan** 
