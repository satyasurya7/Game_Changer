(function ($) {
    "use strict";

    // Navbar on scrolling
    $(window).scroll(function () {
        if ($(this).scrollTop() > 200) {
            $('.navbar').fadeIn('slow').css('display', 'flex');
        } else {
            $('.navbar').fadeOut('slow').css('display', 'none');
        }
    });

    // Smooth scrolling on the navbar links
    $(".navbar-nav a").on('click', function (event) {
        if (this.hash !== "") {
            event.preventDefault();
            
            $('html, body').animate({
                scrollTop: $(this.hash).offset().top - 45
            }, 1500, 'easeInOutExpo');
            
            if ($(this).parents('.navbar-nav').length) {
                $('.navbar-nav .active').removeClass('active');
                $(this).closest('a').addClass('active');
            }
        }
    });

    // Typed Initiate
    if ($('.typed-text-output').length == 1) {
        var typed_strings = $('.typed-text').text();
        var typed = new Typed('.typed-text-output', {
            strings: typed_strings.split(', '),
            typeSpeed: 100,
            backSpeed: 20,
            smartBackspace: false,
            loop: true
        });
    }

    // Modal Video
    $(document).ready(function () {
        var $videoSrc;
        $('.btn-play').click(function () {
            $videoSrc = $(this).data("src");
        });
        console.log($videoSrc);

        $('#videoModal').on('shown.bs.modal', function (e) {
            $("#video").attr('src', $videoSrc + "?autoplay=1&amp;modestbranding=1&amp;showinfo=0");
        })

        $('#videoModal').on('hide.bs.modal', function (e) {
            $("#video").attr('src', $videoSrc);
        })
    });

    // Scroll to Bottom
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.scroll-to-bottom').fadeOut('slow');
        } else {
            $('.scroll-to-bottom').fadeIn('slow');
        }
    });

    // Skills
    $('.skill').waypoint(function () {
        $('.progress .progress-bar').each(function () {
            $(this).css("width", $(this).attr("aria-valuenow") + '%');
        });
    }, {offset: '80%'});

    // Portfolio isotope and filter
    var portfolioIsotope = $('.portfolio-container').isotope({
        itemSelector: '.portfolio-item',
        layoutMode: 'fitRows'
    });
    $('#portfolio-flters li').on('click', function () {
        $("#portfolio-flters li").removeClass('active');
        $(this).addClass('active');

        portfolioIsotope.isotope({filter: $(this).data('filter')});
    });

    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 200) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });

    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        dots: true,
        loop: true,
        items: 1
    });

    // Feedback form submission
    $('#feedbackForm').on('submit', async function(event) {
        event.preventDefault();
        
        const formData = new FormData(event.target);
        const data = {
            name: formData.get('name'),
            subject: formData.get('subject'),
            feedback: formData.get('feedback')
        };    

        console.log(data);  // Add this line to debug and see the data being sent
        
        try {
            const response = await fetch('http://127.0.0.1:8400/feedback', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });
            
            if (response.ok) {
                $('#responseMessage').text('Feedback submitted successfully');
                event.target.reset();
            } else {
                const errorData = await response.json();
                console.error('Error:', errorData);  // Log the server response to see what went wrong
                $('#responseMessage').text('Failed to submit feedback');
            }
        } catch (error) {
            $('#responseMessage').text('An error occurred: ' + error.message);
        }
    });
    // Fetch and display feedback
    async function fetchFeedback() {
        try {
            const response = await fetch('http://127.0.0.1:8400/feedback');
            const feedbackData = await response.json();
            populateFeedback(feedbackData);
        } catch (error) {
            console.error('Error fetching feedback:', error);
        }
    }

    function populateFeedback(feedbackData) {
        const feedbackContainer = $('.owl-carousel.testimonial-carousel');
        feedbackContainer.trigger('destroy.owl.carousel'); // Destroy the previous instance
        feedbackContainer.empty(); // Clear existing items

        feedbackData.forEach(feedback => {
            const feedbackHTML = `
                <div class="text-center">
                    <i class="fa fa-3x fa-quote-left text-primary mb-4"></i>
                    <h4 class="font-weight-light mb-4">${feedback.feedback}</h4>
                    <h5 class="font-weight-bold m-0">${feedback.subject}</h5>
                    <span>${feedback.name}</span>
                </div>
            `;
            feedbackContainer.append(feedbackHTML);
        });

        // Reinitialize the carousel to apply changes
        feedbackContainer.owlCarousel({
            autoplay: true,
            smartSpeed: 1500,
            dots: true,
            loop: true,
            items: 1
        });
    }

    // Call fetchFeedback when the document is ready
    $(document).ready(function() {
        fetchFeedback();
    });
    
})(jQuery);
