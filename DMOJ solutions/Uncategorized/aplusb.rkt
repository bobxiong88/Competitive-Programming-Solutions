#lang racket
(define n (read))
(for ([i (in-range n)])
  (displayln (+ (read) (read))))