; ModuleID = '../src/test40.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test40(i32 %var1, i32 %var2, i32 %var3) #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 %var1, i32* %1, align 4
  store i32 %var2, i32* %2, align 4
  store i32 %var3, i32* %3, align 4
  %4 = load i32* %1, align 4
  %5 = icmp eq i32 %4, 1
  br i1 %5, label %6, label %9

; <label>:6                                       ; preds = %0
  %7 = load i32* %2, align 4
  %8 = add nsw i32 %7, 1
  store i32 %8, i32* %2, align 4
  br label %12

; <label>:9                                       ; preds = %0
  %10 = load i32* %2, align 4
  %11 = add nsw i32 %10, 2
  store i32 %11, i32* %2, align 4
  br label %12

; <label>:12                                      ; preds = %9, %6
  %13 = load i32* %3, align 4
  %14 = icmp eq i32 %13, 2
  br i1 %14, label %15, label %18

; <label>:15                                      ; preds = %12
  %16 = load i32* %2, align 4
  %17 = add nsw i32 %16, 3
  store i32 %17, i32* %2, align 4
  br label %21

; <label>:18                                      ; preds = %12
  %19 = load i32* %2, align 4
  %20 = add nsw i32 %19, 4
  store i32 %20, i32* %2, align 4
  br label %21

; <label>:21                                      ; preds = %18, %15
  %22 = load i32* %2, align 4
  ret i32 %22
}

attributes #0 = { nounwind "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-realign-stack" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"Ubuntu clang version 3.6.2-1 (tags/RELEASE_362/final) (based on LLVM 3.6.2)"}
