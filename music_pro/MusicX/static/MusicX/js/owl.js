$('#slider1, #slider2, #slider3, #slider4, #slider5 ').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 2,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 4,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})


document.querySelector('.trending-header h2').addEventListener('mouseover', () => {
  document.querySelector('.trending-header h2').classList.add('animate-in');
});

document.querySelector('.trending-header h2').addEventListener('mouseout', () => {
  document.querySelector('.trending-header h2').classList.remove('animate-in');
});
