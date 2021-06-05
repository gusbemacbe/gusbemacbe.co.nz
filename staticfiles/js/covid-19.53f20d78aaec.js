const bodyStyles = window.getComputedStyle(document.body);
const colors = 
[
  '--indigo-default',
  '--indigo-dark',
  '--indigo-medium',
  '--indigo-light',
  '--pink-default',
  '--pink-dark',
  '--pink-medium',
  '--pink-light',
  '--cyan-default',
  '--cyan-dark',
  '--cyan-medium',
  '--cyan-light',
  '--cyan-grey-default',
  '--cyan-grey-dark',
  '--cyan-grey-medium',
  '--cyan-grey-light',
];

const colorValues = [];

for (const i = 0; i < colors.length; i++) 
{
  colorValues[colors[i]] = bodyStyles.getPropertyValue(colors[i]);
  consloe.log(colorValues[i]);
}

d3.csv("/static/data/prefeitura-de-aparecida/aparecida-small-without-duplicates.csv").then(makeChart);

// Plot the data with Chart.js
function makeChart(dates) {
  var dateLabels = dates.map(function (d) {
    return d.date;
  });
  var totalDeathsData = dates.map(function (d) {
    return d.totalDeaths;
  });

  var chart = new Chart("myChart", {
    type: "bar",
    data: {
      labels: dateLabels,
      datasets: [
        {
          data: totalDeathsData,
          backgroundColor: colorValue[13]
        }
      ]
    }
  });
}