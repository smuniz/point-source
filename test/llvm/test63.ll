; ModuleID = '../src/test63.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test63(i32 %var1, i32 %var2) #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %n = alloca i32, align 4
  store i32 %var1, i32* %1, align 4
  store i32 %var2, i32* %2, align 4
  store i32 0, i32* %n, align 4
  %3 = load i32* %1, align 4
  switch i32 %3, label %11 [
    i32 1, label %4
    i32 2, label %7
    i32 3, label %8
    i32 4, label %9
    i32 5, label %10
  ]

; <label>:4                                       ; preds = %0
  %5 = load i32* %2, align 4
  %6 = add nsw i32 %5, 1
  store i32 %6, i32* %n, align 4
  br label %11

; <label>:7                                       ; preds = %0
  store i32 2, i32* %n, align 4
  br label %11

; <label>:8                                       ; preds = %0
  store i32 3, i32* %n, align 4
  br label %11

; <label>:9                                       ; preds = %0
  store i32 4, i32* %n, align 4
  br label %11

; <label>:10                                      ; preds = %0
  store i32 5, i32* %n, align 4
  br label %11

; <label>:11                                      ; preds = %0, %10, %9, %8, %7, %4
  %12 = load i32* %n, align 4
  ret i32 %12
}

attributes #0 = { nounwind "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-realign-stack" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"Ubuntu clang version 3.6.2-1 (tags/RELEASE_362/final) (based on LLVM 3.6.2)"}
