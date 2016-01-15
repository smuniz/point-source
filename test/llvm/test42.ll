; ModuleID = '../src/test42.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test42(i32 %var1, i32 %var2) #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %n = alloca i32, align 4
  store i32 %var1, i32* %1, align 4
  store i32 %var2, i32* %2, align 4
  %3 = load i32* %1, align 4
  %4 = icmp eq i32 %3, 1
  br i1 %4, label %5, label %16

; <label>:5                                       ; preds = %0
  store i32 0, i32* %n, align 4
  br label %6

; <label>:6                                       ; preds = %12, %5
  %7 = load i32* %n, align 4
  %8 = icmp slt i32 %7, 10
  br i1 %8, label %9, label %15

; <label>:9                                       ; preds = %6
  %10 = load i32* %2, align 4
  %11 = add nsw i32 %10, 1
  store i32 %11, i32* %2, align 4
  br label %12

; <label>:12                                      ; preds = %9
  %13 = load i32* %n, align 4
  %14 = add nsw i32 %13, 1
  store i32 %14, i32* %n, align 4
  br label %6

; <label>:15                                      ; preds = %6
  br label %16

; <label>:16                                      ; preds = %15, %0
  %17 = load i32* %1, align 4
  %18 = load i32* %2, align 4
  %19 = add nsw i32 %17, %18
  ret i32 %19
}

attributes #0 = { nounwind "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-realign-stack" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"Ubuntu clang version 3.6.2-1 (tags/RELEASE_362/final) (based on LLVM 3.6.2)"}
