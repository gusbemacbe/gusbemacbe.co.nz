// $('.grid').isotope(
// {
//   itemSelector: '.grid-item',
//   columnWidth: '.grid-size',
//   percentPosition: true,
//   masonry:
//   {
//     gutter: 20,
//     horizontalOrder: true,
//     layoutMode: 'fitRows',
//   }
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
      // columnWidth: 40,
      layoutMode: 'packery',
    }
  });

[].forEach.call(document.querySelectorAll('.button'), function (el) {
  el.addEventListener('click', function () {

    const selector = el.getAttribute('data-filter');

    iso.arrange({ filter: selector });

    return false;
  })
})

imagesLoaded('.grid').on( 'progress', function() 
{
  // layout Isotope after each image loads
  iso.layout();
});

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