/** @format */

// async function test() {
//   const a = await 2;
//   const b = await 3;
//   return b;
// }

// test();

require('regenerator-runtime/runtime.js');

require('core-js/modules/es.object.to-string.js');

require('core-js/modules/es.promise.js');

function asyncGeneratorStep(gen, resolve, reject, _next, _throw, key, arg) {
  try {
    var info = gen[key](arg);
    var value = info.value;
  } catch (error) {
    reject(error);
    return;
  }
  if (info.done) {
    resolve(value);
  } else {
    Promise.resolve(value).then(_next, _throw);
  }
}

function _asyncToGenerator(fn) {
  return function () {
    var self = this,
      args = arguments;
    return new Promise(function (resolve, reject) {
      var gen = fn.apply(self, args);
      function _next(value) {
        asyncGeneratorStep(gen, resolve, reject, _next, _throw, 'next', value);
      }
      function _throw(err) {
        asyncGeneratorStep(gen, resolve, reject, _next, _throw, 'throw', err);
      }
      _next(undefined);
    });
  };
}

function test() {
  return _test.apply(this, arguments);
}

function _test() {
  _test = _asyncToGenerator(
    /*#__PURE__*/ regeneratorRuntime.mark(function _callee() {
      var a, b;
      return regeneratorRuntime.wrap(function _callee$(_context) {
        while (1) {
          switch ((_context.prev = _context.next)) {
            case 0:
              _context.next = 2;
              return 2;

            case 2:
              a = _context.sent;
              _context.next = 5;
              return 3;

            case 5:
              b = _context.sent;
              return _context.abrupt('return', b);

            case 7:
            case 'end':
              return _context.stop();
          }
        }
      }, _callee);
    })
  );
  return _test.apply(this, arguments);
}

test();
