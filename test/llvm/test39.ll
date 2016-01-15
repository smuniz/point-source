; ModuleID = '../src/test39.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test39() #0 {
  %local1 = alloca i32, align 4
  %local2 = alloca i32, align 4
  %n = alloca i32, align 4
  %m = alloca i32, align 4
  store i32 0, i32* %n, align 4
  br label %1

; <label>:1                                       ; preds = %17, %0
  %2 = load i32* %n, align 4
  %3 = icmp slt i32 %2, 10
  br i1 %3, label %4, label %20

; <label>:4                                       ; preds = %1
  %5 = load i32* %local2, align 4
  %6 = add nsw i32 %5, 10
  store i32 %6, i32* %local2, align 4
  store i32 0, i32* %m, align 4
  br label %7

; <label>:7                                       ; preds = %13, %4
  %8 = load i32* %m, align 4
  %9 = icmp slt i32 %8, 5
  br i1 %9, label %10, label %16

; <label>:10                                      ; preds = %7
  %11 = load i32* %local1, align 4
  %12 = add nsw i32 %11, 5
  store i32 %12, i32* %local1, align 4
  br label %13

; <label>:13                                      ; preds = %10
  %14 = load i32* %m, align 4
  %15 = add nsw i32 %14, 1
  store i32 %15, i32* %m, align 4
  br label %7

; <label>:16                                      ; preds = %7
  br label %17

; <label>:17                                      ; preds = %16
  %18 = load i32* %n, align 4
  %19 = add nsw i32 %18, 1
  store i32 %19, i32* %n, align 4
  br label %1

; <label>:20                                      ; preds = %1
  %21 = load i32* %local1, align 4
  %22 = load i32* %local2, align 4
  %23 = add nsw i32 %21, %22
  ret i32 %23
}

attributes #0 = { nounwind "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-realign-stack" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"Ubuntu clang version 3.6.2-1 (tags/RELEASE_362/final) (based on LLVM 3.6.2)"}
