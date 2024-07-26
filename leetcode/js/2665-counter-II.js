/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    const counter = {
        start: init, 
        current: init,

        increment: function() {
            this.current += 1;
            return this.current;
        },
        decrement: function() {
            this.current -= 1;
            return this.current;
        },
        reset: function() {
            this.current = this.start;
            return this.current;
        }
    };

    return counter;
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */