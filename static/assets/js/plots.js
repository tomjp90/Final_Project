// Initializes the page with a default plot
// the init function creates some code for us
// notice how init function is called at the end of the code
// in order to restyle a plot we have to have a plot called
// this is where this is a repitition of this data further down 

// this is rooms 
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

  layout = {
    title:  'Vs Average House Price',
    xaxis: {
      title: 'Number of Bedrooms',
      showgrid: false
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
  

  // rooms
  if (dataset === 'dataset1') {
    x = [1, 2, 3, 4, 5, 6];
    y = [435319, 790963, 1053469, 1381954, 1850381, 1937099];
  }

  // bathrooms
  else if (dataset === 'dataset2') {
    x = [1, 2, 3, 4, 5];
    y = [880595, 1196687, 1747261, 2636136, 2667488]; 
  }

  // distance
  else if (dataset === 'dataset3') {
    x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50];
    y = [1185662, 1224077, 1046433, 958513, 808006, 661854, 560663, 735575, 571690, 720314];
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
}

init();
