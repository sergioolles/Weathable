#📱 Weathable (Mobile App)

![Cover](https://github.com/sergioolles/Weathable/assets/123390818/77ef6372-1ca2-4dab-bac4-f65800989c55)

## ℹ️ Table of Contents
- [Introduction](#introduction)
- [Technologies](#technologies)
- [Setup](#setup)
- [Examples of Use](#examples-of-use)
- [Project Status](#project-status)
- [Resources](#resources)

## 🚀 Introduction

Weathable is your go-to outfit assistant that helps you choose the perfect clothing based on the current weather conditions. Whether it's sunny, rainy, or cold, Weathable ensures you're dressed appropriately and comfortably.

Born out of the need for a hassle-free way to select the right outfit for any weather, Weathable provides outfit recommendations tailored to your local weather forecast.

## 🔧 Technologies

Weathable is built using Python 3 and leverages various libraries and APIs to provide real-time weather data and outfit recommendations.

## 💻 Setup

To use Weathable locally, follow these steps:

1. Clone the Weathable repository:
git clone https://github.com/sergioolles/weathable.git

2. Install the required Python packages:

- **requests**: Used to make HTTP requests to the OpenWeatherMap API.
- **csv**: Handles CSV file reading and writing.
- **random**: Used for random item selection.
- **datetime**: Handles date and time-related operations.
- **os**: Provides access to operating system functionality.

3. Obtain an API key from OpenWeatherMap:

- Visit [OpenWeatherMap](https://openweathermap.org/) and sign up for an account if you don't have one.
- After logging in, go to the API Keys section and generate a new API key.
- Copy your API key.

4. Configure Weathable:

- Open the `main.py` file in the Weathable project folder.
- In API_KEY, replace "Insert your API KEY" with your actual OpenWeatherMap API key.
- In CITY, replace the written city, ("Zaragoza"), with the city of your choice.
- In name, replace "Name", with your actual name.
- Save the changes.

5. Configure clothes:
- Use your own clothes! You can download a spreadsheet template for your wardrobe [here](https://docs.google.com/spreadsheets/d/1TseG27LF7cTITzy2Db8nq0QvbWovqDOsl6x6Y2gQJo8/edit?usp=sharing)
- By default, some clothes are on the spreadsheet in order for developers to experiment on new features, like colours, identifiers or descriptions.

6. Run the Weathable application:
python main.py

Weathable will provide different outfit recommendations based on the current weather.

## 📝 Examples of Use

Here are some examples of how to use Weathable:

1. Enter your location. It will fetch the current weather data for your area and recommend an outfit, including tops, bottoms, shoes and overtops if necessary.
2. Weathable takes into account temperature, precipitation, and other weather factors to ensure your outfit is both weather-appropriate.
3. Use Weathable to plan your outfits for the day and never worry about what to wear in changing weather conditions.

Running the program gives you a different outfit each time, since the code randomly selects different clothing elements, out of the available depending on the weather. This is replicated in the prototype adding a "Next Outfit" button.

## ✅ Project Status

Weathable is a developed and finished project, providing a reliable solution for outfit recommendations based on local weather conditions. It is fully functional and ready for use.

### 🧩 Next Steps

While Weathable is complete, there are several exciting enhancements that can be considered for future iterations:

- **Adding Other Categories:** Expand the clothing categories to include winter and summer accessories, hats, and more, providing users with even more outfit choices.

- **Automated Location Based on User's Location:** Implement location detection to automatically retrieve the user's location without manual input, enhancing user convenience.

- **Taking Into Account Different Colors:** Consider incorporating color analysis to make outfit recommendations that not only consider the weather but also the user's style preferences.

- **Support for Multiple Languages:** Extend Weathable's usability by adding support for multiple languages, making it accessible to a wider audience.
  
- **Mobile App Development**: Create a JavaScript file or use a framework like React Native to convert the existing Python code into a mobile app. This will allow users to access the outfit recommendations on their smartphones, making it more convenient and user-friendly.

## 👉 Resources

### 🌟 Weathable Brand & Guidelines

[Weathable Branding Presentation](https://www.figma.com/proto/o4JZU6pwRHMrXf0IGbXMRy/Weathable-Brand?page-id=0%3A1&type=design&node-id=29-1186&viewport=2694%2C2055%2C0.11&t=XDbCB8A7ehtOBFze-1&scaling=contain&starting-point-node-id=29%3A1192&mode=design)

![Cover](https://github.com/sergioolles/Weathable/assets/123390818/b399d33a-8ef8-4072-a976-d37355d07ac5)

### 🎨 Weathable Mobile App

[Weathable Figma Protype](https://www.figma.com/proto/qEKcu093GfmRwMRIQEq6qo/Weathable-App?page-id=0%3A1&type=design&node-id=29-1402&viewport=-18%2C748%2C0.73&t=QgETLf8uwa9HNkZT-1&scaling=scale-down&starting-point-node-id=29%3A1402&mode=design)

![Slide 13 - Mobile App](https://github.com/sergioolles/Weathable/assets/123390818/cb356c68-d7af-4cb2-aa62-f3f3a75f1598)

