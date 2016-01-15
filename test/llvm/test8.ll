; ModuleID = '../src/test8.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test8(i32 %value1) #0 {
  %1 = alloca i32, align 4
  %local1 = alloca i32, align 4
  store i32 %value1, i32* %1, align 4
  %2 = load i32* %1, align 4
  %3 = icmp sgt i32 %2, 5
  br i1 %3, label %4, label %7

; <label>:4                                       ; preds = %0
  %5 = load i32* %1, align 4
  %6 = add nsw i32 %5, 10
  store i32 %6, i32* %local1, align 4
  br label %10

; <label>:7                                       ; preds = %0
  %8 = load i32* %1, align 4
  %9 = add nsw i32 %8, 20
  store i32 %9, i32* %local1, align 4
  br label %10

; <label>:10                                      ; preds = %7, %4
  %11 = load i32* %local1, align 4
  ret i32 %11
}

attributes #0 = { nounwind "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-realign-stack" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"Ubuntu clang version 3.6.2-1 (tags/RELEASE_362/final) (based on LLVM 3.6.2)"}
