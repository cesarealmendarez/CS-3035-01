grader :: Float -> Float -> String
grader score1 score2
  | avgScore >= 90.0 = "A"
  | avgScore >= 80.0 = "B"
  | otherwise = "C"
  where avgScore = (score1 + score2) / 2.0


-- fibonacci :: Int -> Int
-- fibonacci 0 = 0
-- fibonacci 1 = 1
-- fibonacci n = fibonacci (n - 1) + fibonacci (n - 2)


