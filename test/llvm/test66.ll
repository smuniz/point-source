; ModuleID = '../src/test66.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test66(i32 %var1, i32 %var2) #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %result = alloca i32, align 4
  store i32 %var1, i32* %1, align 4
  store i32 %var2, i32* %2, align 4
  %3 = load i32* %1, align 4
  %4 = icmp eq i32 %3, 2
  br i1 %4, label %5, label %7

; <label>:5                                       ; preds = %0
  %6 = load i32* %1, align 4
  store i32 %6, i32* %result, align 4
  br label %9

; <label>:7                                       ; preds = %0
  %8 = load i32* %2, align 4
  store i32 %8, i32* %result, align 4
  br label %9

; <label>:9                                       ; preds = %7, %5
  %10 = load i32* %result, align 4
  ret i32 %10
}

attributes #0 = { nounwind "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-realign-stack" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"Ubuntu clang version 3.6.2-1 (tags/RELEASE_362/final) (based on LLVM 3.6.2)"}
