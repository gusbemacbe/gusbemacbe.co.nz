const agesCSV = async () => 
{
  const array = []
  await d3.csv("/static/data/gustavo/confirmados/aparecida-casos-por-faixa-etária.csv", data => { array.push(data)});
  return array;
}

const agesChart = async () => 
{
  const ages = await agesCSV()

  const cases = _.filter(ages, "isDeath");
  const { FEMININO: femaleCases, MASCULINO: maleCases } = _.groupBy(
    cases,
    "sex"
  );

  const maleCasesByAge = _.groupBy(maleCases, ({ age }) => {
    const ageInRange = _.inRange.bind(_, age);

    switch (true) {
      case ageInRange(0, 15):
        return "child";
      case ageInRange(15, 20):
        return "teeneger";
      case ageInRange(20, 50):
        return "adult";
      case ageInRange(50, 60):
        return "matureAdult";
      case ageInRange(60, 120):
        return "oldMan";
    }
  });

  const femaleCasesByAge = _.groupBy(femaleCases, ({ age }) => {
    const ageInRange = _.inRange.bind(_, age);

    switch (true) {
      case ageInRange(0, 15):
        return "child";
      case ageInRange(15, 20):
        return "teeneger";
      case ageInRange(20, 50):
        return "adult";
      case ageInRange(50, 60):
        return "matureAdult";
      case ageInRange(60, 120):
        return "oldWoman";
    }
  });

  const maleConfirmedByAge = {
    child: [],
    teeneger: [],
    adult: [],
    matureAdult: [],
    oldMan: [],
    ...maleCasesByAge,
  };

  const femaleConfirmedByAge = {
    child: [],
    teeneger: [],
    adult: [],
    matureAdult: [],
    oldWoman: [],
    ...femaleCasesByAge,
  };

  console.log(
    _.map(maleConfirmedByAge, "length"), // o que vc quer é esse int aqui
    _.map(maleConfirmedByAge, (value, key) => key), // a ordem das labels vai ser essa
    _.map(femaleConfirmedByAge, "length"), // o que vc quer é esse int aqui
    _.map(femaleConfirmedByAge, (value, key) => key) // a ordem das labels vai ser essa
  );

  const cases_by_age = new Chart('CasesbyAge',
  {
    type: "bar",
    data: 
    {
      labels: ["0-15", "15-20", "20-50", "50-60", "60+", "Sem idade"],
      datasets: 
      [
        {
          color: "rgba(226, 117, 169, 1)",
          backgroundColor: "rgba(226, 117, 169, 1)",
          data: _.map(femaleConfirmedByAge, "length"),
          label: "Female"
        },
        {
          color: "rgba(113, 205, 248, 1)",
          backgroundColor: "rgba(113, 205, 248, 1)",
          data: _.map(maleConfirmedByAge, "length"),
          label: "Male"
        }
      ]
    },
    options: 
    {
      indexAxis: 'y',
      elements: {
        bar: {
          borderWidth: 2,
        }
      },
      plugins: 
      {
        title: 
        {
            color: "rgba(198, 216, 217, 1)",
            display: true,
            text: 'Casos por idade etária'
        }
      },
      responsive: true,
      scales: 
      {
        yAxes: 
        [{
            stacked: true
        }],
        xAxes: 
        [{
            stacked: false
        }]
      }
    },
  })

}

agesChart();