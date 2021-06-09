const bodyStyles = window.getComputedStyle(document.body);
const colours = [ "--indigo-default", "--indigo-dark", "--indigo-medium", "--indigo-light", "--pink-default", "--pink-dark", "--pink-medium", "--pink-light", "--cyan-default", "--cyan-dark", "--cyan-medium", "--cyan-light", "--cyan-grey-default", "--cyan-grey-dark", "--cyan-grey-medium", "--cyan-grey-light"];

const colourValues = [];

for (let c = 0; c < colours.length; c++) 
{
  colourValues[colours] = bodyStyles.getPropertyValue(colours);
}