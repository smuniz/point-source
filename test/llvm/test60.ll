; ModuleID = '../src/test60.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test60(i32 %value) #0 {
  %1 = alloca i32, align 4
  store i32 %value, i32* %1, align 4
  %2 = load i32* %1, align 4
  %3 = icmp eq i32 %2, 1
  br i1 %3, label %4, label %5

; <label>:4                                       ; preds = %0
  br label %12

; <label>:5                                       ; preds = %0
  br label %6

; <label>:6                                       ; preds = %12, %5
  %7 = load i32* %1, align 4
  %8 = icmp eq i32 %7, 2
  br i1 %8, label %9, label %15

; <label>:9                                       ; preds = %6
  %10 = load i32* %1, align 4
  %11 = add nsw i32 %10, 2
  store i32 %11, i32* %1, align 4
  br label %12

; <label>:12                                      ; preds = %9, %4
  %13 = load i32* %1, align 4
  %14 = add nsw i32 %13, 1
  store i32 %14, i32* %1, align 4
  br label %6

; <label>:15                                      ; preds = %6
  %16 = load i32* %1, align 4
  ret i32 %16
}

attributes #0 = { nounwind "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-realign-stack" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"Ubuntu clang version 3.6.2-1 (tags/RELEASE_362/final) (based on LLVM 3.6.2)"}
