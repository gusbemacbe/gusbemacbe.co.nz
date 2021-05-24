const attribute = (name) => (element) => element.getAttribute(name);
const ariaControls = attribute('aria-controls');

const toggleAttribute = (attribute) => (element) => {
  const attributeState = element.getAttribute(attribute) === 'true';
  element.setAttribute(attribute, attributeState ? 'false' : 'true');
};

const toggleAriaExpanded = toggleAttribute('aria-expanded');

function initOffCanvas (trigger) {
  const offcanvasTrigger = document.querySelector(trigger);
  const triggerOffcanvas = ariaControls(offcanvasTrigger);
  const offcanvas = document.getElementById(triggerOffcanvas);

  const toggleMobileMenu = toggleAriaExpanded.bind(null, offcanvas);
  offcanvasTrigger.addEventListener('click', toggleMobileMenu);
}

function initOffCanvasSubmenus (selector) {
  const triggers = document.querySelectorAll(selector);
  triggers.forEach((trigger) => {
    const toggleSubmenu = toggleAriaExpanded.bind(null, trigger);

    trigger.addEventListener('click', toggleSubmenu);
  });
}

document.addEventListener('DOMContentLoaded', () => {
  initOffCanvas('.hamburger');
  initOffCanvasSubmenus('.menu-link[aria-controls]');
});