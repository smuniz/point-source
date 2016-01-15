; ModuleID = '../src/test67.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test67(i32 %value1) #0 {
  %1 = alloca i32, align 4
  %local1 = alloca i32, align 4
  store i32 %value1, i32* %1, align 4
  store i32 1, i32* %local1, align 4
  %2 = load i32* %1, align 4
  %3 = and i32 %2, 5
  %4 = icmp ne i32 %3, 0
  br i1 %4, label %5, label %8

; <label>:5                                       ; preds = %0
  %6 = load i32* %1, align 4
  %7 = add nsw i32 %6, 10
  store i32 %7, i32* %local1, align 4
  br label %8

; <label>:8                                       ; preds = %5, %0
  %9 = load i32* %local1, align 4
  ret i32 %9
}

attributes #0 = { nounwind "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-realign-stack" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"Ubuntu clang version 3.6.2-1 (tags/RELEASE_362/final) (based on LLVM 3.6.2)"}
