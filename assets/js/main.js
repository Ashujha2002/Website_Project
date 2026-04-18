/***************************************************
==================== JS INDEX ======================
****************************************************
GSAP Registration
Animations Initialize
Preloader
Data Bg JS
Header Search
Heder Sticky
Mobile Menu
Offcanvas Menu
Nice Select
GLightBox JS
Progress bar
Swiper Sliders
Project Masonry
Pricing Toggle
Counter
Chart
Contact Map
Copyright Year
CountDown
Cursor
GSAP Animations


****************************************************/

(function ($) {
	"use strict";

	////////////////////////////////////////////////////
	// GSAP Registration
	if (typeof gsap !== "undefined") {
		gsap.registerPlugin(ScrollTrigger, ScrollSmoother, ScrollToPlugin, SplitText);
	}

	////////////////////////////////////////////////////
	// Animations Initialize
	window.gsapAnimations = function () {
		initGlobalFadeAnimations();
		initPxnZoom();
		initSplitTextAnimations();
		initPxnCharsUp();
		initPxnImageReveal();
		initPxnZoomIn();
		initPxnHoverButtons();
		initPxnBgParallax();
		initPxnCharsReveal();
	};

	////////////////////////////////////////////////////
	// Preloader
	$(window).on("load", function () {
		const pxnPreloader = $("#pxn-preloader");
		if (pxnPreloader.length > 0) {
			setTimeout(function () {
				pxnPreloader.addClass("is-loaded");
				pxnPreloader.fadeOut(600);
				gsapAnimations();
			}, 1000);
		} else {
			gsapAnimations();
		}
	});

	////////////////////////////////////////////////////
	// Data Bg JS
	$("[data-bg-image]").each(function () {
		$(this).css("background-image", "url(" + $(this).attr("data-bg-image") + ")");
	});

	////////////////////////////////////////////////////
	// Header Search
	$(".pxn_header_search").on("click", function () {
		$(".pxn_search_popup").addClass("search-opened");
		$(".pxn_search_popup_overlay").addClass("opened");
	});
	$(".search_close_btn").on("click", function () {
		$(".pxn_search_popup").removeClass("search-opened");
		$(".pxn_search_popup_overlay").removeClass("opened");
	});
	$(".pxn_search_popup_overlay").on("click", function () {
		$(".pxn_search_popup").removeClass("search-opened");
		$(this).removeClass("opened");
	});

	////////////////////////////////////////////////////
	// Heder Sticky
	var lastScrollTop = "";
	function stickyMenu($targetMenu, $toggleClass) {
		var st = $(window).scrollTop();
		if ($(window).scrollTop() > 500) {
			if (st > lastScrollTop) {
				$targetMenu.removeClass($toggleClass);
			} else {
				$targetMenu.addClass($toggleClass);
			}
		} else {
			$targetMenu.removeClass($toggleClass);
		}

		lastScrollTop = st;
	}

	$(window).on("scroll", function () {
		if ($(".pxn-header").length) {
			stickyMenu($(".header-sticky"), "sticky");
		}
	});

	////////////////////////////////////////////////////
	// Mobile Menu
	if ($("#mobile-menu").length) {
		$("#mobile-menu").meanmenu({
			meanMenuContainer: ".mobile_menu",
			meanScreenWidth: "991",
			meanExpand: ['<i class="pxni-angle-down"></i>'],
		});
	}

	////////////////////////////////////////////////////
	// Offcanvas Menu
	if ($(".pxn_offcanvas").length) {
		$(".pxn_offcanvas_toggle").on("click", function () {
			$(".pxn_offcanvas").addClass("opened");
			$(".pxn_offcanvas_overlay").addClass("opened");
		});

		$(".offcanvas_close").on("click", function () {
			$(".pxn_offcanvas").removeClass("opened");
			$(".pxn_offcanvas_overlay").removeClass("opened");
		});
		$(".pxn_offcanvas_overlay").on("click", function () {
			$(".pxn_offcanvas").removeClass("opened");
			$(this).removeClass("opened");
		});
	}

	////////////////////////////////////////////////////
	// Nice Select
	if ($(".pxn-select").length > 0) {
		$(".pxn-select").niceSelect();
	}

	////////////////////////////////////////////////////
	// GLightBox JS
	const videoPopup = GLightbox({
		selector: ".video_popup",
		touchNavigation: false,
	});

	const pxnImageGallery = GLightbox({
		selector: "[data-gallery]",
		touchNavigation: true,
		loop: true,
		zoomable: true,
		autoplayVideos: true,
	});

	////////////////////////////////////////////////////
	// Progress bar
	function initProgressBars() {
		$(".pxn_progress").each(function () {
			const container = $(this);
			const bar = container.find(".progress_bar");
			const percentText = container.find(".progress_percent");

			const percent = parseInt(bar.data("percent")) || 0;

			// start state
			bar.css("width", "0%");

			function animateBar() {
				if (bar.hasClass("animated")) return;

				bar.addClass("animated");

				$({ value: 0 }).animate(
					{ value: percent },
					{
						duration: 1200,
						step: function (val) {
							bar.css("width", val + "%");

							if (percentText.length) {
								percentText.text(Math.round(val) + "%");
							}
						},
					}
				);
			}

			// basic scroll detection
			$(window).on("scroll", function () {
				const top = container.offset().top;
				const scroll = $(window).scrollTop() + $(window).height();

				if (scroll > top) {
					animateBar();
				}
			});
		});
	}
	initProgressBars();

	////////////////////////////////////////////////////
	// Swiper Sliders

	// Post Thumb Slider
	if ($(".pxn_post_thumb_slider").length > 0) {
		var h3TestimonialCarousel = new Swiper(".pxn_post_thumb_slider", {
			slidesPerView: 1,
			spaceBetween: 0,
			loop: true,
			speed: 1200,
			autoplay: {
				delay: 3000,
				disableOnInteraction: false,
			},
			navigation: {
				nextEl: ".pxn_slider-next",
				prevEl: ".pxn_slider-prev",
			},
		});
	}

	// H1 Hero Slider
	if ($(".pxn-h1-hero-slider").length > 0) {
		var h1HeroSlider = new Swiper(".pxn-h1-hero-slider", {
			slidesPerView: 1,
			spaceBetween: 0,
			effect: "fade",
			loop: true,
			speed: 1500,
			autoplay: {
				delay: 3000,
			},
			// navigation: {
			// 	nextEl: ".pxn_slider-next",
			// 	prevEl: ".pxn_slider-prev",
			// },
			pagination: {
				el: ".pxn_slider-pagination",
				clickable: true,
			},
		});
	}

	// H1 Client Carousel
	if ($(".pxn-h1_client_carousel").length > 0) {
		var h1ClientCarousel = new Swiper(".pxn-h1_client_carousel", {
			slidesPerView: 6,
			spaceBetween: 12,
			loop: true,
			speed: 2000,
			allowTouchMove: false,
			autoplay: {
				delay: 3000,
				disableOnInteraction: false,
			},
			breakpoints: {
				0: {
					slidesPerView: 2,
					spaceBetween: 15,
				},
				576: {
					slidesPerView: 2,
					spaceBetween: 20,
				},
				768: {
					slidesPerView: 3,
					spaceBetween: 20,
				},
				992: {
					slidesPerView: 4,
				},
				1400: {
					slidesPerView: 5,
				},
			},
		});
	}

	// H1 Testimonial Carousel
	if ($(".pxn-h1_testimonial_carousel").length > 0) {
		var h1TestimonialCarousel = new Swiper(".pxn-h1_testimonial_carousel", {
			slidesPerView: "auto",
			spaceBetween: 24,
			loop: true,
			speed: 1200,
			autoplay: {
				delay: 3000,
				disableOnInteraction: false,
			},
			pagination: {
				el: ".pxn_slider-pagination",
				clickable: true,
			},
		});
	}

	// H2 Testimonial Carousel
	if ($(".pxn-h2_testimonial_carousel").length > 0) {
		var h1TestimonialCarousel = new Swiper(".pxn-h2_testimonial_carousel", {
			slidesPerView: "auto",
			spaceBetween: 24,
			loop: true,
			speed: 1200,
			autoplay: {
				delay: 3000,
				disableOnInteraction: false,
			},
			pagination: {
				el: ".pxn_slider-pagination",
				clickable: true,
			},
		});
	}

	// H3 Testimonial Carousel
	if ($(".pxn-h3_testimonial_carousel").length > 0) {
		var h3TestimonialCarousel = new Swiper(".pxn-h3_testimonial_carousel", {
			slidesPerView: 1,
			spaceBetween: 24,
			loop: true,
			speed: 1200,
			autoplay: {
				delay: 3000,
				disableOnInteraction: false,
			},
			pagination: {
				el: ".pxn_slider-pagination",
				clickable: true,
			},
		});
	}

	////////////////////////////////////////////////////
	// Project Masonry
	if ($(".pxn-h1_projects_wrap").length > 0) {
		var $grid = $(".grid").masonry({
			itemSelector: ".grid-item",
			percentPosition: true,
			columnWidth: ".grid-sizer",
		});
		// layout Masonry after each image loads
		$grid.imagesLoaded().progress(function () {
			$grid.masonry();
		});
	}

	////////////////////////////////////////////////////
	// Pricing Toggle
	if ($(".pxn-toggle-checkbox").length > 0) {
		$(".pxn-toggle-checkbox").on("change", function () {
			var $card = $(".pxn_pricing_box");
			var $price = $card.find(".price");
			var $period = $card.find(".period");

			if ($(this).is(":checked")) {
				$price.text($price.data("year-price"));
				$period.text($period.data("year-period"));
			} else {
				$price.text($price.data("month-price"));
				$period.text($period.data("month-period"));
			}
		});
	}

	////////////////////////////////////////////////////
	// Counter
	if ($(".pxn_counter-number").length > 0) {
		function animateCounter($el) {
			var from = parseFloat($el.data("from-value")) || 0;
			var to = parseFloat($el.data("to-value")) || 0;
			var duration = parseInt($el.data("duration")) || 2000;

			$({ counter: from }).animate(
				{ counter: to },
				{
					duration: duration,
					easing: "swing",
					step: function (now) {
						$el.text(Math.floor(now));
					},
					complete: function () {
						$el.text(to);
					},
				}
			);
		}

		// Trigger on scroll (only once)
		var observer = new IntersectionObserver(
			function (entries, obs) {
				entries.forEach(function (entry) {
					if (entry.isIntersecting) {
						var $el = $(entry.target);
						animateCounter($el);
						obs.unobserve(entry.target);
					}
				});
			},
			{ threshold: 0.5 }
		);

		$(".pxn_counter-number").each(function () {
			observer.observe(this);
		});
	}

	////////////////////////////////////////////////////
	// Chart
	if ($(".pxn-chart").length > 0) {
		document.querySelectorAll(".pxn-chart").forEach(function (canvas) {
			const type = canvas.dataset.type || "doughnut";
			const size = canvas.dataset.size || 220;
			const dataValues = canvas.dataset.data ? canvas.dataset.data.split(",").map(Number) : [40, 40, 20];

			const bgColors = canvas.dataset.colors ? canvas.dataset.colors.split("|") : ["#ddd", "#bbb", "#999"];

			const spacing = canvas.dataset.spacing ? Number(canvas.dataset.spacing) : 0;

			const cutout = canvas.dataset.cutout ? canvas.dataset.cutout + "%" : "60%";

			const tooltipsEnabled = canvas.dataset.tooltips !== "false";

			// Apply dynamic size
			// canvas.parentElement.style.width = size + "px";
			// canvas.parentElement.style.height = size + "px";

			new Chart(canvas, {
				type: type,
				data: {
					datasets: [
						{
							data: dataValues,
							backgroundColor: bgColors,
							spacing: spacing,
							borderWidth: 0,
						},
					],
				},
				options: {
					responsive: true,
					maintainAspectRatio: false,
					cutout: cutout,
					plugins: {
						legend: {
							display: false,
						},
						tooltip: {
							enabled: tooltipsEnabled,
						},
					},
				},
			});
		});
	}

	////////////////////////////////////////////////////
	// Contact Map
	const maps = document.querySelectorAll(".pxn-map");
	maps.forEach(mapEl => {
		const config = JSON.parse(mapEl.dataset.map || "{}");

		const lat = parseFloat(config.lat) || 0;
		const lng = parseFloat(config.lng) || 0;
		const zoom = parseInt(config.zoom) || 14;
		const icon = config.icon || "pxni-map-pin";

		const map = L.map(mapEl, {
			center: [lat, lng],
			zoom: zoom,
			zoomControl: false,
		});

		L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png", {
			attribution: "&copy; OpenStreetMap contributors",
		}).addTo(map);

		const customMarker = L.divIcon({
			className: "pxn_map_marker",
			html: `<i class="${icon}"></i>`,
			iconSize: [40, 40],
			iconAnchor: [20, 40],
		});

		L.marker([lat, lng], {
			icon: customMarker,
		}).addTo(map);
	});

	////////////////////////////////////////////////////
	// Copyright Year
	if ($(".pxn_copyright_text").length > 0) {
		const yearEl = document.querySelector(".pxn_copyright_text span");

		if (yearEl) {
			const currentYear = new Date().getFullYear();
			const spanYear = parseInt(yearEl.textContent);

			if (spanYear < currentYear) {
				yearEl.textContent = currentYear;
			}
		}
	}

	////////////////////////////////////////////////////
	// CountDown
	class PxnCountdown {
		constructor(el) {
			this.el = el;
			this.date = new Date(el.dataset.date).getTime();

			this.stop = el.dataset.stop === "true";

			this.labels = {
				days: el.dataset.days || "Days",
				hours: el.dataset.hours || "Hours",
				minutes: el.dataset.minutes || "Minutes",
				seconds: el.dataset.seconds || "Seconds",
			};

			this.expireTitle = el.dataset.expireTitle || "";
			this.expireDesc = el.dataset.expireDesc || "";

			this.start();
		}

		start() {
			if (this.stop) {
				this.el.innerHTML = this.timerContent({
					days: "08",
					hours: "12",
					minutes: "30",
					seconds: "45",
				});
				return;
			}

			this.update();
			this.interval = setInterval(() => this.update(), 1000);
		}

		// add leading zero
		format(num) {
			return num < 10 ? "0" + num : num;
		}

		update() {
			const now = new Date().getTime();
			const distance = this.date - now;

			if (distance < 0) {
				clearInterval(this.interval);
				this.el.innerHTML = this.expireContent();
				return;
			}

			const days = Math.floor(distance / (1000 * 60 * 60 * 24));
			const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
			const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
			const seconds = Math.floor((distance % (1000 * 60)) / 1000);

			this.el.innerHTML = this.timerContent({
				days: this.format(days),
				hours: this.format(hours),
				minutes: this.format(minutes),
				seconds: this.format(seconds),
			});
		}

		timerContent(times) {
			let html = "";

			Object.keys(times).forEach(key => {
				html += `
				<div class="timer-content timer-item-${key}">
					<span class="time-count ${key}-count">${times[key]}</span>
					<span class="time-title ${key}-title">${this.labels[key]}</span>
				</div>
				<span class="divider">:</span>
			`;
			});

			return html;
		}

		expireContent() {
			let html = `<div class="countdown-expire">`;

			if (this.expireTitle) {
				html += `<div class="countdown-expire-title">${this.expireTitle}</div>`;
			}

			if (this.expireDesc) {
				html += `<div class="countdown-expire-desc">${this.expireDesc}</div>`;
			}

			html += `</div>`;
			return html;
		}
	}

	// init all countdowns
	document.querySelectorAll(".pxn-countdown").forEach(el => {
		new PxnCountdown(el);
	});

	////////////////////////////////////////////////////
	// Cursor
	if ($(".mouse-cursor").length && $(".cursor-inner").length && $(".cursor-outer").length) {
		const inner = document.querySelector(".cursor-inner");
		const outer = document.querySelector(".cursor-outer");

		if (!inner || !outer) return;

		// Hide on mobile / touch devices
		if (window.matchMedia("(pointer: coarse)").matches) {
			inner.style.display = "none";
			outer.style.display = "none";
			return;
		}

		let cursorVisible = false;

		window.addEventListener("mousemove", function (e) {
			outer.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;
			inner.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;

			if (!cursorVisible) {
				inner.classList.add("cursor-visible");
				outer.classList.add("cursor-visible");

				inner.classList.remove("cursor-hidden");
				outer.classList.remove("cursor-hidden");

				cursorVisible = true;
			}
		});

		// Hide when leaving browser window
		document.addEventListener("mouseleave", function () {
			inner.classList.remove("cursor-visible");
			outer.classList.remove("cursor-visible");

			inner.classList.add("cursor-hidden");
			outer.classList.add("cursor-hidden");

			cursorVisible = false;
		});

		// Show when entering again
		document.addEventListener("mouseenter", function () {
			inner.classList.add("cursor-visible");
			outer.classList.add("cursor-visible");

			inner.classList.remove("cursor-hidden");
			outer.classList.remove("cursor-hidden");

			cursorVisible = true;
		});

		$("body").on("mouseenter", "a, .know_tm_topbar .trigger, .cursor-pointer", function () {
			inner.classList.add("cursor-hover");
			outer.classList.add("cursor-hover");
		});

		$("body").on("mouseleave", "a, .know_tm_topbar .trigger, .cursor-pointer", function () {
			if (!($(this).is("a") && $(this).closest(".cursor-pointer").length)) {
				inner.classList.remove("cursor-hover");
				outer.classList.remove("cursor-hover");
			}
		});
	}

	////////////////////////////////////////////////////
	// Form Submission
	if ($("#contact-form").length > 0) {
		$("#contact-form").validate({
			rules: {
				conName: "required",
				conEmail: {
					required: true,
					email: true,
				},
				conPhone: "required",
				conMessage: "required",
			},

			messages: {
				conName: "Enter your full name.",
				conEmail: "Enter your valid email address.",
				conPhone: "Enter your valid phone number.",
				conMessage: "Enter your query message.",
			},
			submitHandler: function (form) {
				// start ajax request
				$.ajax({
					type: "POST",
					url: "assets/mail/contact-form.php",
					data: $("#contact-form").serialize(),
					cache: false,
					success: function (data) {
						if (data == "Y") {
							$("#message_sent").modal("show");
							$("#contact-form").trigger("reset");
						} else {
							$("#message_fail").modal("show");
						}
					},
				});
			},
		});
	}

	/*********************************************************************************************************
======================================== GSAP Animations ==========================================
*********************************************************************************************************/

	// Smooth Scroll
	if ($("#smooth-wrapper").length && $("#smooth-content").length && ScrollTrigger.isTouch !== 1) {
		gsap.config({ nullTargetWarn: false });

		if (!ScrollSmoother.get()) {
			window.pxnSmoother = ScrollSmoother.create({
				smooth: 1,
				effects: true,
				smoothTouch: 0.1,
				normalizeScroll: false,
				ignoreMobileResize: true,
			});
		}
	}

	// match media
	let mediaMatch = gsap.matchMedia();

	// Fade Animation
	function initGlobalFadeAnimations() {
		const fadeItems = gsap.utils.toArray(".pxn-fade");
		if (!fadeItems.length) return;

		const isRTL = document.documentElement.dir === "rtl"; // detect RTL

		fadeItems.forEach(item => {
			// Read data attributes
			const onscroll = parseInt(item.getAttribute("data-on-scroll")) || 1;
			const offset = parseInt(item.getAttribute("data-offset")) || 40;
			const delay = parseFloat(item.getAttribute("data-delay")) || 0.15;
			const duration = parseFloat(item.getAttribute("data-duration")) || 1.15;
			const direction = item.getAttribute("data-direction") || "bottom";
			const easeValue = item.getAttribute("data-ease") || "power2.out";

			// Determine initial x/y based on direction
			let x = 0,
				y = 0;

			switch (direction.toLowerCase()) {
				case "left":
					x = isRTL ? offset : -offset;
					break;
				case "right":
					x = isRTL ? -offset : offset;
					break;
				case "top":
					y = -offset;
					break;
				case "bottom":
					y = offset;
					break;
			}

			// Base animation settings
			const animSettings = {
				autoAlpha: 0,
				x: x,
				y: y,
				ease: easeValue,
				duration: duration,
				delay: delay,
			};

			// Add ScrollTrigger if required
			if (onscroll === 1 && typeof ScrollTrigger !== "undefined") {
				animSettings.scrollTrigger = {
					trigger: item,
					start: "top 85%",
					// you can add toggleActions, markers for debugging
					// toggleActions: "play none none none",
					// invalidateOnRefresh: true,
				};
			}

			// Set initial state visible to prevent flash
			gsap.set(item, { autoAlpha: 1 });

			// Run animation
			gsap.from(item, animSettings);
		});
	}

	// Zoom Animation
	function initPxnZoom() {
		const zoomItems = gsap.utils.toArray(".pxn-zoom");

		if (!zoomItems.length) return;

		zoomItems.forEach(item => {
			let onscrollValue = item.getAttribute("data-on-scroll") || 1,
				startScale = item.getAttribute("data-scale") || 0.5,
				delayValue = item.getAttribute("data-delay") || 0,
				durationValue = item.getAttribute("data-duration") || 1,
				easeValue = item.getAttribute("data-ease") || "power2.out";

			let animationSetting = {
				scale: startScale,
				autoAlpha: 0,
				duration: durationValue,
				delay: delayValue,
				ease: easeValue,
			};

			if (onscrollValue == 1) {
				animationSetting.scrollTrigger = {
					trigger: item,
					start: "top 85%",
				};
			}

			gsap.set(item, { autoAlpha: 1 });

			gsap.from(item, animationSetting);
		});
	}

	// Split Text
	function initSplitTextAnimations() {
		const splitTextElements = gsap.utils.toArray(".pxn-split-text");
		if (!splitTextElements.length) return;

		const isRTL = document.documentElement.dir === "rtl"; // detect RTL

		splitTextElements.forEach(element => {
			// Read data attributes
			let staggerAmount = parseFloat(element.getAttribute("data-stagger")) || 0.02;
			let translateXValue = parseFloat(element.getAttribute("data-x")) || 30;
			const translateYValue = parseFloat(element.getAttribute("data-y")) || 0;
			const delayValue = parseFloat(element.getAttribute("data-delay")) || 0.3;
			const durationValue = parseFloat(element.getAttribute("data-duration")) || 1;
			const easeType = element.getAttribute("data-ease") || "power2.out";

			// Flip X in RTL
			if (isRTL) translateXValue = -translateXValue;

			// Split text
			const splitInstance = new SplitText(element, {
				type: "chars, words",
				charsClass: "pxn-char",
				wordsClass: "pxn-word",
			});

			// Animate characters
			gsap.from(splitInstance.chars, {
				duration: durationValue,
				delay: delayValue,
				x: translateXValue,
				y: translateYValue,
				autoAlpha: 0,
				ease: easeType,
				stagger: staggerAmount,
				scrollTrigger: {
					// markers: true,
					trigger: element,
					start: "top 85%",
					invalidateOnRefresh: true,
				},
			});
		});
	}

	// Chars up
	function initPxnCharsUp() {
		const elements = gsap.utils.toArray(".pxn-chars-up");
		if (!elements.length) return;

		const isRTL = document.documentElement.dir === "rtl";

		elements.forEach(element => {
			const split = new SplitText(element, {
				type: "chars,lines",
				charsClass: "pxn-char",
				linesClass: "pxn-line",
			});

			// Prevent char overflow
			gsap.set(split.lines, { overflow: "hidden" });

			const tl = gsap.timeline({
				scrollTrigger: {
					trigger: element,
					start: "top 85%",
					toggleActions: "play none none none",
				},
			});

			tl.from(split.chars, {
				yPercent: 100,
				duration: 0.35,
				ease: "power2.out",
				stagger: {
					amount: 0.6,
					from: isRTL ? "end" : "start",
				},
			});
		});
	}

	// Chars reveal
	function initPxnCharsReveal() {
		const elements = gsap.utils.toArray(".pxn-chars-reveal");
		if (!elements.length) return;

		const isRTL = document.documentElement.dir === "rtl";

		elements.forEach(element => {
			const split = new SplitText(element, {
				type: "lines,words,chars",
				linesClass: "pxn-line",
				wordsClass: "pxn-word",
				charsClass: "pxn-char",
			});

			// Initial state
			gsap.set(split.chars, {
				opacity: 0.3,
				x: isRTL ? 7 : -7, // RTL support
			});

			gsap.to(split.chars, {
				x: 0,
				y: 0,
				opacity: 1,
				duration: 0.7,
				ease: "power2.out",
				stagger: 0.03,

				scrollTrigger: {
					trigger: element,
					start: "top 90%",
					end: "top 60%",
					scrub: 1.2,
					once: true,
				},
			});
		});
	}

	// Image reveal
	function initPxnImageReveal() {
		// Select all image reveal containers
		const revealItems = gsap.utils.toArray(".pxn-img-reveal");

		if (!revealItems.length) return;

		const isRTL = document.documentElement.dir === "rtl";

		revealItems.forEach(container => {
			const image = container.querySelector("img");
			if (!image) return;

			// Timeline for this element
			const tl = gsap.timeline({
				scrollTrigger: {
					trigger: container,
					start: "top 70%",
					// invalidateOnRefresh: true,
				},
			});

			// Make container visible
			tl.set(container, { autoAlpha: 1 });

			// Slide in container from left
			tl.from(container, {
				duration: 1.5,
				xPercent: isRTL ? 100 : -100,
				ease: "power2.out",
			});

			// Slide image from right + scale
			tl.from(image, {
				duration: 1.5,
				xPercent: isRTL ? -100 : 100,
				scale: 1.3,
				ease: "power2.out",
				delay: -1.5, // overlap with container animation
			});
		});
	}

	// Image zoom in
	function initPxnZoomIn() {
		const zoomItems = gsap.utils.toArray(".pxn-zoom-in");

		if (!zoomItems.length) return;

		zoomItems.forEach(element => {
			// Wrap element in a container for overflow hidden if not already wrapped
			if (!element.parentElement.classList.contains("pxn-zoom-in-wrap")) {
				const wrap = document.createElement("div");
				wrap.classList.add("pxn-zoom-in-wrap");
				wrap.style.overflow = "hidden";

				element.parentNode.insertBefore(wrap, element);
				wrap.appendChild(element);
			}

			const container = element.parentElement;

			// Timeline with ScrollTrigger
			const tl = gsap.timeline({
				scrollTrigger: {
					trigger: container,
					start: "top 90%",
					markers: false,
					// invalidateOnRefresh: true,
				},
			});

			// Animate element
			tl.from(element, {
				duration: 1.5,
				// autoAlpha: 0,
				scale: 1.15,
				ease: "power2.out",
				clearProps: "all", // removes inline styles after animation
			});
		});
	}

	// Hover buttons
	function initPxnHoverButtons() {
		const wrappers = gsap.utils.toArray(".pxn-hover-btn-wrapper");
		const items = gsap.utils.toArray(".pxn-hover-btn-item");

		if (!wrappers.length || !items.length) return;

		wrappers.forEach((wrapper, i) => {
			const target = items[i];
			if (!target) return;

			// Mouse move event
			wrapper.addEventListener("mousemove", e => {
				parallaxMove(e, wrapper, target, 30);
			});

			// Mouse leave event → reset
			wrapper.addEventListener("mouseleave", () => {
				gsap.to(target, {
					duration: 1,
					x: 0,
					y: 0,
					ease: "power2.out",
				});
			});
		});

		// Parallax calculation
		function parallaxMove(e, wrapper, target, movement) {
			const rect = wrapper.getBoundingClientRect();
			const relX = e.clientX - rect.left;
			const relY = e.clientY - rect.top;

			gsap.to(target, {
				duration: 1,
				x: ((relX - rect.width / 2) / rect.width) * movement,
				y: ((relY - rect.height / 2) / rect.height) * movement,
				ease: "power2.out",
			});
		}
	}

	// Image parallax
	function initPxnBgParallax() {
		const items = gsap.utils.toArray(".pxn-img-parallax");

		if (!items.length) return;

		items.forEach(el => {
			const speed = parseFloat(el.dataset.speed) || 40;

			// Set initial background
			gsap.set(el, {
				backgroundPosition: "50% 0%",
			});

			gsap.to(el, {
				backgroundPosition: `50% ${speed}%`,
				ease: "none",
				scrollTrigger: {
					trigger: el,
					start: "top bottom",
					end: "bottom top",
					scrub: true,
				},
			});
		});
	}
})(jQuery);
