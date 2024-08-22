Basic Air Pollution monitoring and Visualization using NodeMCU\

Hardware Requirements : NodeMCU, Gas sensor, WiFi connection\

Software Requirements: Python, JupyterLab.\

Step one: Assemble the device.\

Step two: The NodeMCU will send the data to https://thingspeak.com/ where it will be logged and saved. Create a acc there and a logging point. Then modify the NodeMCU .ino file, including the specific keys.Remember to add the Wifi access point and password.\

Step three: Log the data by deploying the device.\

Step four: Download the logged data from thingspeak, it will be in .csv format. Place it on the root folder of the repo and run JupyterLab, it will automatically visualize the data for you. You might need to rename the places.\
