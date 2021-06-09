const datesCSV = async () => 
{
  const array = []
  await d3.csv("/static/data/prefeitura-de-aparecida/aparecida-small-without-duplicates.csv", data => { array.push(data)});
  return array;
}

const makeChart = async () => 
{
  const dates = await datesCSV()
  const dateLabels = dates.map(d => new Date(d.date))

  const totalDeathsData = dates.map(d => d.totalDeaths)
  const totalCasesData = dates.map(d => d.totalCases)
  const totalRecoveredData = dates.map(d => d.totalRecovered)

  const DailyDeathsData = dates.map((item, index) => {
    if (index === 0) return 0;
    return dates[index].totalDeaths - dates[index - 1].totalDeaths
  });

  const DailyCasesData = dates.map((item, index) => {
    if (index === 0) return 0;
    return dates[index].totalCases - dates[index - 1].totalCases
  });

  const DailyRecoveredData = dates.map((item, index) => {
    if (index === 0) return 0;
    return dates[index].totalRecovered - dates[index - 1].totalRecovered
  });

  const activeCases = dates.map((item, index) => {
    if (index === 0) return 0;
    return dates[index].totalCases - dates[index].totalRecovered
  });

  const totalBedsData = dates.map(d => d.totalBeds)
  const totalICUData = dates.map(d => d.intubated)
  
  Chart.defaults.font.size = 16
  Chart.defaults.font.family = "'Exo 2', sans-serif"

  const formatTick = (month) => 
  {
    switch (true) 
    {
      case month.includes("Jan"):
        return month
      case month.includes("Feb"):
        return month.replace("Feb", "Fev").split(" ")[0];
      case month.includes("Mar"):
        return month.replace("Mar", "Mar").split(" ")[0];
      case month.includes("Apr"):
        return month.replace("Apr", "Abr").split(" ")[0];
      case month.includes("May"):
        return month.replace("May", "Maio").split(" ")[0];
      case month.includes("Jun"):
        return month.replace("Jun", "Jun").split(" ")[0];
      case month.includes("Jul"):
        return month.replace("Jul", "Jul").split(" ")[0];
      case month.includes("Aug"):
        return month.replace("Aug", "Ago").split(" ")[0];
      case month.includes("Sep"):
        return month.replace("Sep", "Set").split(" ")[0];
      default:
        return month
    }
  };

  let temp = ''
  const total_number = new Chart('TotalNumber',
  {
    type: "bar",
    data: 
    {
      labels: dateLabels,
      datasets: 
      [
        {
          color: "rgba(226, 117, 169, 1)",
          backgroundColor: "rgba(226, 117, 169, 1)",
          borderColor: "rgba(226, 117, 169, 1)",
          data: totalDeathsData,
          label: "Número cumulativo da mortes"
        },
        {
          color: "rgba(113, 205, 248, 1)",
          backgroundColor: "rgba(113, 205, 248, 1)",
          borderColor: "rgba(113, 205, 248, 1)",
          data: totalRecoveredData,
          label: "Número cumulativo de recuperados"
        },
        {
          color: "rgba(198, 216, 217, 1)",
          backgroundColor: "rgba(198, 216, 217, 1)",
          borderColor: "rgba(198, 216, 217, 1)",
          data: totalCasesData,
          label: "Número cumulativo de casos."
        }
      ]
    },
    options: 
    {
      adapters: 
      {
        date: 
        {
            locale: "pt"
        }
      },
      plugins: 
      {
        legend: 
        {
          labels: 
          {
            color: "rgba(221, 232, 232, 1)",
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
          text: 'Núemros cumulativos de casos, mortes e recuperados'
        },
      },
      responsive: true,
      scales: 
      {
        xAxes: 
        {
          type: 'time',
          time: 
          {
            unit: "month",
            tooltipFormat: "dd/MM/yyyy",
          },
          ticks: 
          {
            color: "rgba(198, 216, 217, 1)",
            callback: formatTick
          },
          grid: 
          {
            color: "rgba(99, 108, 109, 1)",
            borderColor: "rgba(99, 108, 109, 1)",
            borderWidth: 0.15,
            tickColor: "rgba(99, 108, 109, 1)"
          },
          stacked: true,
        },
        yAxes: 
        {
          grid: 
          {
            color: "rgba(99, 108, 109, 1)",
            borderColor: "rgba(99, 108, 109, 1)",
            borderWidth: 0.15,
            tickColor: "rgba(99, 108, 109, 1)"
          },
          stacked: true
        }
      }
    }
  });
  
  const daily_number = new Chart('DailyNumber',
  {
    type: "bar",
    data: 
    {
      labels: dateLabels,
      datasets: 
      [
        {
          color: "rgba(226, 117, 169, 1)",
          backgroundColor: "rgba(226, 117, 169, 1)",
          borderColor: "rgba(226, 117, 169, 1)",
          data: DailyDeathsData,
          label: "Número diário de mortes"
        },
        {
          color: "rgba(113, 205, 248, 1)",
          backgroundColor: "rgba(113, 205, 248, 1)",
          borderColor: "rgba(113, 205, 248, 1)",
          data: DailyRecoveredData,
          label: "Número diário de recuperados"
        },
        {
          color: "rgba(198, 216, 217, 1)",
          backgroundColor: "rgba(198, 216, 217, 1)",
          borderColor: "rgba(198, 216, 217, 1)",
          data: DailyCasesData,
          label: "Número diário de casos"
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
              color: "rgba(221, 232, 232, 1)",
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
          text: 'Números diários de casos, mortes e recuperados'
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
            tooltipFormat: "dd/MM/yyyy",
            unit: 'month'
          },
          ticks: 
          {
            color: "rgba(198, 216, 217, 1)",
            callback: formatTick
          },
          grid: 
          {
            color: "rgba(99, 108, 109, 1)",
            borderColor: "rgba(99, 108, 109, 1)",
            borderWidth: 0.15,
            tickColor: "rgba(99, 108, 109, 1)"
          },
          stacked: true,
        },
        y: 
        {
          grid: 
          {
            color: "rgba(99, 108, 109, 1)",
            borderColor: "rgba(99, 108, 109, 1)",
            borderWidth: 0.15,
            tickColor: "rgba(99, 108, 109, 1)"
          },
          stacked: true
        }
      }
    }
  })
  
  const activeCasesNumber = new Chart('ActiveCasesNumber',
  {
    type: "bar",
    data: 
    {
      labels: dateLabels,
      datasets: 
      [
        {
          color: "rgba(113, 205, 248, 1)",
          backgroundColor: "rgba(113, 205, 248, 1)",
          borderColor: "rgba(113, 205, 248, 1)",
          data: activeCases,
          label: "Casos ativos"
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
              color: "rgba(221, 232, 232, 1)",
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
          text: 'Número de casos ativos'
        }
      },
      responsive: true,
      scales: 
      {
        x: 
        {
          type: 'time',
          time: 
          {tooltipFormat: "dd/MM/yyyy",
            unit: 'month'
          },
          ticks: 
          {
            color: "rgba(198, 216, 217, 1)",
            callback: formatTick
          },
          grid: 
          {
            color: "rgba(99, 108, 109, 1)",
            borderColor: "rgba(99, 108, 109, 1)",
            borderWidth: 0.15,
            tickColor: "rgba(99, 108, 109, 1)"
          },
          stacked: true,
        },
        y: 
        {
          grid: 
          {
            color: "rgba(99, 108, 109, 1)",
            borderColor: "rgba(99, 108, 109, 1)",
            borderWidth: 0.15,
            tickColor: "rgba(99, 108, 109, 1)"
          },
          stacked: true
        }
      }
    }
  })

  const beds_number = new Chart('BedsNumber',
  {
    type: "bar",
    data: 
    {
      labels: dateLabels,
      datasets: 
      [
        {
          color: "rgba(226, 117, 169, 1)",
          backgroundColor: "rgba(226, 117, 169, 1)",
          borderColor: "rgba(226, 117, 169, 1)",
          data: totalICUData,
          label: "Número diário de UTIs"
        },
        {
          color: "rgba(113, 205, 248, 1)",
          backgroundColor: "rgba(113, 205, 248, 1)",
          borderColor: "rgba(113, 205, 248, 1)",
          data: totalBedsData,
          label: "Número diário de leitos ocupados"
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
              color: "rgba(221, 232, 232, 1)",
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
          text: 'Números diários de leitos ocupados e UTIs'
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
            tooltipFormat: "dd/MM/yyyy",
            unit: 'month'
          },
          ticks: 
          {
            color: "rgba(198, 216, 217, 1)",
            callback: formatTick
          },
          grid: 
          {
            color: "rgba(99, 108, 109, 1)",
            borderColor: "rgba(99, 108, 109, 1)",
            borderWidth: 0.15,
            tickColor: "rgba(99, 108, 109, 1)"
          },
          stacked: true,
        },
        y: 
        {
          grid: 
          {
            color: "rgba(99, 108, 109, 1)",
            borderColor: "rgba(99, 108, 109, 1)",
            borderWidth: 0.15,
            tickColor: "rgba(99, 108, 109, 1)"
          },
          stacked: true
        }
      }
    }
  });
}

makeChart();
