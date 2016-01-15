; ModuleID = '../src/test59.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test59(i32 %param1, i32 %param2) #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %n = alloca i32, align 4
  %m = alloca i32, align 4
  store i32 %param1, i32* %1, align 4
  store i32 %param2, i32* %2, align 4
  br label %3

; <label>:3                                       ; preds = %8, %0
  %4 = load i32* %2, align 4
  %5 = icmp eq i32 %4, 5
  br i1 %5, label %6, label %7

; <label>:6                                       ; preds = %3
  store i32 1, i32* %1, align 4
  br label %11

; <label>:7                                       ; preds = %3
  br label %8

; <label>:8                                       ; preds = %7
  %9 = load i32* %2, align 4
  %10 = icmp ne i32 %9, 0
  br i1 %10, label %3, label %11

; <label>:11                                      ; preds = %8, %6
  %12 = load i32* %1, align 4
  %13 = load i32* %2, align 4
  %14 = add nsw i32 %12, %13
  ret i32 %14
}

attributes #0 = { nounwind "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-realign-stack" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"Ubuntu clang version 3.6.2-1 (tags/RELEASE_362/final) (based on LLVM 3.6.2)"}
