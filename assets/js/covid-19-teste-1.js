// @ts-check
/**
 * @typedef {Object} CsvPerson
 * @property {string} city
 * @property {string} ibge_code
 * @property {string} age
 * @property {"FEMININO"|"MASCULINO"} sex
 * @property {string} sympthom_starting_date
 * @property {"0"|"1"} isDeath
 */

/** @type {<T>(predicates: ((item: T) => boolean)[]) => (array: T) => boolean} */
const conditions = (predicates) => (item) => {
  return predicates.map((predicate) => predicate(item)).every(Boolean);
};

/** @param {CsvPerson} param0 */
const isMale = ({ sex }) => sex === "MASCULINO";

/** @param {CsvPerson} param0 */
const isFemale = ({ sex }) => sex === "FEMININO";

/** @param {CsvPerson} param0 */
const isAdult = ({ age }) => +age > 19 && +age < 60;

/** @param {CsvPerson} param0 */
const isDead = ({ isDeath }) => !!Number(isDeath);

const isDeadAdultMale = conditions([isDead, isMale, isAdult]);

/** @type {CsvPerson[]} */
const data = [
  {
    sex: "MASCULINO",
    age: "18",
    isDeath: "1",
    city: "Aparecida",
    ibge_code: "11111",
    sympthom_starting_date: "1111",
  },
  {
    sex: "FEMININO",
    age: "21",
    isDeath: "1",
    city: "Aparecida",
    ibge_code: "11111",
    sympthom_starting_date: "1111",
  },
  {
    sex: "MASCULINO",
    age: "21",
    isDeath: "0",
    city: "Aparecida",
    ibge_code: "11111",
    sympthom_starting_date: "1111",
  },
  {
    sex: "MASCULINO",
    age: "21",
    isDeath: "1",
    city: "Aparecida",
    ibge_code: "11111",
    sympthom_starting_date: "1111",
  },
];

const deadAdultMales = data.filter(isDeadAdultMale);