function carousel() {
  return {
    slide: 0,
    slidesAmount: 0,
    init() {
      const wrapper = this.$refs.wrapper;
      const slides = wrapper.querySelectorAll(".carousel__slide");
      this.slidesAmount = slides.length;
    },
    isSafeNextIndex(index) {
      return index < this.slidesAmount;
    },
    isSafePreviousIndex(index) {
      return index > 0;
    },
    next() {
      const nextSlide = this.slide + 1;
      this.slide = this.isSafeNextIndex(nextSlide) ? nextSlide : 0;
    },
    previous() {
      const nextSlide = this.slide - 1;
      this.slide = this.isSafePreviousIndex(nextSlide)
        ? nextSlide
        : this.slidesAmount - 1;
    },
  };
}