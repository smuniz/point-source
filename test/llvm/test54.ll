; ModuleID = '../src/test54.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test54(i32 %var1) #0 {
  %1 = alloca i32, align 4
  %n = alloca i32, align 4
  store i32 %var1, i32* %1, align 4
  store i32 0, i32* %n, align 4
  br label %2

; <label>:2                                       ; preds = %11, %0
  %3 = load i32* %1, align 4
  %4 = icmp sgt i32 %3, 10
  br i1 %4, label %5, label %6

; <label>:5                                       ; preds = %2
  store i32 20, i32* %1, align 4
  br label %6

; <label>:6                                       ; preds = %5, %2
  %7 = load i32* %n, align 4
  %8 = add nsw i32 %7, 1
  store i32 %8, i32* %n, align 4
  %9 = load i32* %1, align 4
  %10 = add nsw i32 %9, -1
  store i32 %10, i32* %1, align 4
  br label %11

; <label>:11                                      ; preds = %6
  %12 = load i32* %n, align 4
  %13 = icmp slt i32 %12, 10
  br i1 %13, label %2, label %14

; <label>:14                                      ; preds = %11
  %15 = load i32* %1, align 4
  ret i32 %15
}

attributes #0 = { nounwind "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-realign-stack" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"Ubuntu clang version 3.6.2-1 (tags/RELEASE_362/final) (based on LLVM 3.6.2)"}
