; ModuleID = '../src/test55.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test55(i32 %value1, i32 %value2, i32 %value3) #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %local1 = alloca i32, align 4
  store i32 %value1, i32* %1, align 4
  store i32 %value2, i32* %2, align 4
  store i32 %value3, i32* %3, align 4
  store i32 0, i32* %local1, align 4
  %4 = load i32* %1, align 4
  %5 = icmp eq i32 %4, 1
  br i1 %5, label %6, label %9

; <label>:6                                       ; preds = %0
  %7 = load i32* %2, align 4
  %8 = icmp eq i32 %7, 1
  br i1 %8, label %15, label %9

; <label>:9                                       ; preds = %6, %0
  %10 = load i32* %1, align 4
  %11 = icmp ne i32 %10, 1
  br i1 %11, label %12, label %16

; <label>:12                                      ; preds = %9
  %13 = load i32* %3, align 4
  %14 = icmp eq i32 %13, 1
  br i1 %14, label %15, label %16

; <label>:15                                      ; preds = %12, %6
  store i32 10, i32* %local1, align 4
  br label %17

; <label>:16                                      ; preds = %12, %9
  store i32 1, i32* %local1, align 4
  br label %17

; <label>:17                                      ; preds = %16, %15
  %18 = load i32* %local1, align 4
  ret i32 %18
}

attributes #0 = { nounwind "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-realign-stack" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"Ubuntu clang version 3.6.2-1 (tags/RELEASE_362/final) (based on LLVM 3.6.2)"}
