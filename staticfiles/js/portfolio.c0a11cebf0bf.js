// $('.grid').isotope(
// {
//   itemSelector: '.grid-item',
//   layoutMode: 'fitRows',
// });

// $('.button').click(function() 
// {
//   $('.button').removeClass('active');
//   $(this).addClass('active');

//   const selector = $(this).attr('data-filter');
//   $('.grid').isotope(
//     {
//       filter: selector
//     }
//   );
//   return false;
// })

const iso = new Isotope('.grid',
  {
    itemSelector: '.grid-item',
    percentPosition: true,
    masonry:
    {
      columnWidth: 240,
      gutter: 10,
      horizontalOrder: true,
      layoutMode: 'fitRows',
    }
  });

[].forEach.call(document.querySelectorAll('.button'), function (el) {
  el.addEventListener('click', function () {

    // el.querySelector('.active').classList.remove('active');
    // el.classList.add('active');

    const selector = el.getAttribute('data-filter');

    iso.arrange({ filter: selector });

    return false;
  })
})

// change is-checked class on buttons
const buttonGroups = document.querySelectorAll('.button-group');
for (const i = 0, len = buttonGroups.length; i < len; i++) {
  const buttonGroup = buttonGroups[i];
  radioButtonGroup(buttonGroup);
}

function radioButtonGroup (buttonGroup) {
  buttonGroup.addEventListener('click', function (event) {
    // only work with buttons
    if (!matchesSelector(event.target, 'button')) {
      return;
    }
    buttonGroup.querySelector('.active').classList.remove('active');
    event.target.classList.add('active');
  });
}