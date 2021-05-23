// Initializes the page with a default plot
// the init function creates some code for us
// notice how init function is called at the end of the code
// in order to restyle a plot we have to have a plot called
// this is where this is a repitition of this data further down 

// this is rooms // bedrooms
function init() {
  data = [{
    x: [1, 2, 3, 4, 5, 6],
    y: [435319, 790963, 1053469, 1381954, 1850381, 1937099],
    mode: 'lines',
    line: {
      color: 'rgb(0, 204, 153)',
      width: 3
    }
  
    }];
  

  // layout = {
  //   title:  'Bedrooms Vs Average House Price'
  // };

  layout = {
    title:  'Bedrooms Vs Average House Price',
    xaxis: {
      title: 'Number of Bedrooms',
      showgrid: false,
      tickmode: "linear", //  If "linear", the placement of the ticks is determined by a starting position `tick0` and a tick step `dtick`
      tick0: 1,
      dtick: 1
    },
    yaxis: {
      title: 'Average House Price $m',
      showline: false
    },
    // makes the background colour transparent
    paper_bgcolor: 'rgba(0,0,0,0)',
    plot_bgcolor: 'rgba(0,0,0,0)'
  };


  Plotly.newPlot("lineplots", data, layout);
}

// Call updatePlotly() when a change takes place to the DOM
// selDataset is from the html file
// so whenever this changes we update the plotly function
// updatePlotly gets a ref to our selector then gets the current selected value
// go and gets the values of whichever is selected of dataset1 or dataset2
d3.selectAll("#selDataset").on("change", updatePlotly);

// This function is called when a dropdown menu item is selected
function updatePlotly() {
  // Use D3 to select the dropdown menu
  var dropdownMenu = d3.select("#selDataset");
  // Assign the value of the dropdown menu option to a variable
  var dataset = dropdownMenu.property("value");

  // Initialize x and y arrays
  var x = [];
  var y = [];
  var title = "";
  var xaxis = "";
  var tick0, dtick; 
  

  // bedrooms
  if (dataset === 'dataset1') {
    x = [1, 2, 3, 4, 5, 6];
    y = [435319, 790963, 1053469, 1381954, 1850381, 1937099];
    title = "Bedrooms Vs Average House Price";
    xaxis = "Bed";
    tick0 = 1;
    dtick = 1;
  }

  // bathrooms
  else if (dataset === 'dataset2') {
    x = [1, 2, 3, 4, 5];
    y = [880595, 1196687, 1747261, 2636136, 2667488]; 
    title = "Bathrooms Vs Average House Price";
    xaxis = "Bath";
    tick0 = 1;
    dtick = 1;
  }

  // distance
  else if (dataset === 'dataset3') {
    x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50];
    y = [1185662, 1224077, 1046433, 958513, 808006, 661854, 560663, 735575, 571690, 720314];
    title = "Distance Vs Average House Price";
    xaxis = "Distance";
    tick0 = 5;
    dtick = 5;
  }

  // landsize
  else if (dataset === 'dataset4') {
    x = [200, 400, 600, 800, 1000, 1200, 1400];
    y = [796182, 1112400, 1067106, 1241597, 1465269, 1336483, 1834727];
    title = "Land Size Vs Average House Price";
    xaxis = "Land";
    tick0 = 200;
    dtick = 200;
  }

  // Note the extra brackets around 'x' and 'y'
  // we are passing x and y into an array cos when we initially created our plot, our data was an array of traces
  // https://plotly.com/javascript/plotlyjs-function-reference/#plotlyrestyle
  
  // restyle - rather than redrawing entire image, it just restyles an element of it
  // restyle only modifies - in this case the x vales of the plot "x"
  Plotly.restyle("lineplots", "x", [x]);
  // and in this case modifies the y values of the plot "y"
  //only modifies the bare essentials that we need to make our plot update 
  Plotly.restyle("lineplots", "y", [y]);
  // Plotly.restyle("lineplots", "title", [title]);
  // update only values within nested objects
  var update = {
    title: title,
    xaxis: {
      title: xaxis,
      tick0: tick0,
      dtick: dtick
    }
  };
  Plotly.relayout("lineplots", update) 
}

init();
