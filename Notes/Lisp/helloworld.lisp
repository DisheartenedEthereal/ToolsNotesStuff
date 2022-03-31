(defun fact (n)
  (if (< n 2)
      1
    (* n (fact(- n 1)))))

(format t (fact 5))

