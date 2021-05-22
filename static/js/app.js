// var button = d3.select("#scrape-btn");
// var form = d3.select("#domainWebsite");
// // create event handlers for button and form
// button.on("click", runEnter);
// form.on("submit", runEnter);

// function runEnter() {
//       d3.event.preventDefault();

//       var inputElement = d3.select("#domainWebsite");
//       var inputValue = inputElement.property("value");

//       console.log(inputValue)

//       var split_domain = inputValue.split('au/')[1]

//       console.log(split_domain)

//       api_route = `http://127.0.0.1:5000/api/v1.0/${split_domain}`

//       console.log(api_route)
// }

// d3.json(api_route).then((data) => {


// }

var button = d3.select("#doCheckPrediction");
button.on("click", graphing);
// scrape = d3.select("#predictionValue").node().value;
// d3.select("#doCheckPrediction").on("click", (event) => graphing(event));

function graphing(){
      data = { msg }   
       
      console.log(data)


}



