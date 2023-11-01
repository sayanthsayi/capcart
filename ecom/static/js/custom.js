$(document).ready(function () {
    $('.increment').click(function (e) { 
        e.preventDefault();

        let value = $('.prod_qty').val()
        
        if (value<10){
            value++
            $('.prod_qty').val(value)
        }
        console.log(value)
        
    });

    $('.decrement').click(function (e) { 
        e.preventDefault();

        let value =$('.prod_qty').val()

        if(value>1){
            value--

            $('.prod_qty').val(value)

            console.log(value)
        }
    });

    $('.cart_btn').click(function (e) { 
        e.preventDefault();

        let id =$('.prod_id').val()

        let qty = $('.prod_qty').val()
        let token = $('input[name=csrfmiddlewaretoken]').val()

        $.ajax({
            type: "POST",
            url: "/cart/AddToCart/",
            data: {
                'id':id,
                'qty':qty,
                csrfmiddlewaretoken :token

            },
            dataType: "json",
            success: function (response) {
                alert(response.status)
            }
        }); 
    });
    $('.wishlist_btn').click(function (e) { 
        e.preventDefault();

        let id =$('.prod_id').val()
        let token = $('input[name=csrfmiddlewaretoken]').val()

        $.ajax({
            type: "POST",
            url: "/cart/AddToishlist/",
            data: {
                'id':id,
                csrfmiddlewaretoken :token
            },
            dataType: "json",
            success: function (response) {
                alert(response.status)
            }
        }); 
    });

});

function animateFrom(elem, direction) {
    direction = direction || 1;
    var x = 0,
        y = direction * -100;
    if(elem.classList.contains("gs_reveal_fromLeft")) {
      x = 100;
      y = 0;
    } else if (elem.classList.contains("gs_reveal_fromRight")) {
      x = -100;
      y = 0;
    }
    elem.style.transform = "translate(" + x + "px, " + y + "px)";
    elem.style.opacity = "0";
    gsap.fromTo(elem, {x: x, y: y, autoAlpha: 0}, {
      duration: 4.25, 
      x: 0,
      y: 0, 
      autoAlpha: 1, 
      ease: "expo", 
      overwrite: "auto"
    });
  }
  
function hide(elem) {
    gsap.set(elem, {autoAlpha: 0});
  }
  
  document.addEventListener("DOMContentLoaded", function() {
    gsap.registerPlugin(ScrollTrigger);
    
    gsap.utils.toArray(".gs_reveal").forEach(function(elem) {
      hide(elem); // assure that the element is hidden when scrolled into view
      
      ScrollTrigger.create({
        trigger: elem,
        // markers: true,
        onEnter: function() { animateFrom(elem,10) }, 
        onEnterBack: function() { animateFrom(elem, -1) },
        onLeave: function() { hide(elem,) } // assure that the element is hidden when scrolled into view
      });
    });
  });


// search

const searchFocus = document.getElementById('search-focus');
const keys = [
  { keyCode: 'AltLeft', isTriggered: false },
  { keyCode: 'ControlLeft', isTriggered: false },
];

window.addEventListener('keydown', (e) => {
  keys.forEach((obj) => {
    if (obj.keyCode === e.code) {
      obj.isTriggered = true;
    }
  });

  const shortcutTriggered = keys.filter((obj) => obj.isTriggered).length === keys.length;

  if (shortcutTriggered) {
    searchFocus.focus();
  }
});

window.addEventListener('keyup', (e) => {
  keys.forEach((obj) => {
    if (obj.keyCode === e.code) {
      obj.isTriggered = false;
    }
  });
});


