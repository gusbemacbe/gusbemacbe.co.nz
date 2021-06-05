const bodyStyles = window.getComputedStyle(document.body);
const colours = [ "--indigo-default", "--indigo-dark", "--indigo-medium", "--indigo-light", "--pink-default", "--pink-dark", "--pink-medium", "--pink-light", "--cyan-default", "--cyan-dark", "--cyan-medium", "--cyan-light", "--cyan-grey-default", "--cyan-grey-dark", "--cyan-grey-medium", "--cyan-grey-light"];

const colourValues = [];

for (let c = 0; c < colours.length; c++) 
{
  colourValues[colours] = bodyStyles.getPropertyValue(colours);
}

const readCsv = async () => 
{
  const array = []
  await d3.csv("/static/data/prefeitura-de-aparecida/aparecida-small-without-duplicates.csv", data => { array.push(data)});
  return array;
}

const makeChart = async () => 
{
  const dates = await readCsv()
  const dateLabels = dates.map(d => new Date(d.date))

  const totalDeathsData = dates.map(d => d.totalDeaths)
  const totalCasesData = dates.map(d => d.totalCases)
  const totalRecoveredData = dates.map(d => d.totalRecovered)

  // const DailyDeathsData = dates.reduce((v1, v2) => { return v1.totalDeaths - v2.totalDeaths });
  // const DailyCasesData = dates.slice(1).map((v, j) => v.totalCases - dates[j].totalCases);
  // const DailyRecoveredData = dates.slice(1).map((v, j) => v.totalRecovered - dates[j].totalRecovered);

  Chart.defaults.font.size = 16
  Chart.defaults.font.family = "'Exo 2', sans-serif"

  let temp = ''
  const total_number = new Chart(document.getElementById('TotalNumber').getContext('2d'),
  {
    type: "bar",
    data: 
    {
      labels: dateLabels,
      datasets: 
      [
        {
          color: colourValues[colours[7]],
          backgroundColor: colourValues[colours[7]],
          borderColor: colourValues[colours[7]],
          data: totalDeathsData,
          label: "Total Death"
        },
        {
          color: colourValues[colours[3]],
          backgroundColor: colourValues[colours[3]],
          borderColor: colourValues[colours[3]],
          data: totalRecoveredData,
          label: "Total Recovered"
        },
        {
          color: colourValues[colours[11]],
          backgroundColor: colourValues[colours[11]],
          borderColor: colourValues[colours[11]],
          data: totalCasesData,
          label: "Total Cases"
        }
      ]
    },
    options: 
    {
      plugins: 
      {
        legend: 
        {
            labels: 
            {
              color: colourValues[colours[15]],
              font: 
              {
                  family: "'Exo 2', sans-serif",
                  size: 14
              }
            }
        },
        title: 
        {
          display: false,
          text: 'Total Deaths'
        },
        tooltip: 
        {
   
        }
      },
      responsive: true,
      scales: 
      {
        x: 
        {
          type: 'time',
          time: 
          {
            unit: 'month'
          },
          ticks: 
          {
            color: colourValues[colours[12]],
            callback: function(value, index) {
              if (value.includes("Jan"))
                return value;
              return value.split(" ")[0]
            }
          },
          grid: 
          {
            color: colourValues[colours[14]],
            borderColor: colourValues[colours[14]],
            borderWidth: 0.15,
            tickColor: colourValues[colours[14]]
          },
          stacked: true,
        },
        y: 
        {
          grid: 
          {
            color: colourValues[colours[14]],
            borderColor: colourValues[colours[14]],
            borderWidth: 0.15,
            tickColor: colourValues[colours[14]]
          },
          stacked: true
        }
      }
    }
  });
  
  // const daily_number = new Chart('DailyNumber',
  // {
  //   type: "bar",
  //   data: 
  //   {
  //     labels: dateLabels,
  //     datasets: 
  //     [
  //       {
  //         color: colourValues[colours[7]],
  //         backgroundColor: colourValues[colours[7]],
  //         borderColor: colourValues[colours[7]],
  //         data: DailyDeathsData,
  //         label: "Daily Deaths"
  //       },
  //       {
  //         color: colourValues[colours[3]],
  //         backgroundColor: colourValues[colours[3]],
  //         borderColor: colourValues[colours[3]],
  //         data: DailyRecoveredData,
  //         label: "Daily Recovered"
  //       },
  //       {
  //         color: colourValues[colours[11]],
  //         backgroundColor: colourValues[colours[11]],
  //         borderColor: colourValues[colours[11]],
  //         data: DailyCasesData,
  //         label: "Daily Cases"
  //       }
  //     ]
  //   },
  //   options: 
  //   {
  //     plugins: 
  //     {
  //       legend: 
  //       {
  //           labels: 
  //           {
  //             color: colourValues[colours[15]],
  //             font: 
  //             {
  //                 family: "'Exo 2', sans-serif",
  //                 size: 14
  //             }
  //           }
  //       },
  //       title: 
  //       {
  //         display: false,
  //         text: 'Daily Number'
  //       }
  //     },
  //     responsive: true,
  //     scales: 
  //     {
  //       x: 
  //       {
  //         type: 'time',
  //         time: 
  //         {
  //           unit: 'month'
  //         },
  //         ticks: 
  //         {
  //           color: colourValues[colours[12]],
  //           callback: function(value, index) {
  //             if (value.includes("Jan"))
  //               return value;
  //             return value.split(" ")[0]
  //           }
  //         },
  //         grid: 
  //         {
  //           color: colourValues[colours[14]],
  //           borderColor: colourValues[colours[14]],
  //           borderWidth: 0.15,
  //           tickColor: colourValues[colours[14]]
  //         },
  //         stacked: true,
  //       },
  //       y: 
  //       {
  //         grid: 
  //         {
  //           color: colourValues[colours[14]],
  //           borderColor: colourValues[colours[14]],
  //           borderWidth: 0.15,
  //           tickColor: colourValues[colours[14]]
  //         },
  //         stacked: true
  //       }
  //     }
  //   }
  // })
}

makeChart();
