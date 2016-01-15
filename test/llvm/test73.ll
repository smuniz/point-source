; ModuleID = '../src/test73.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test73a(i32 %value1) #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %local1 = alloca i32, align 4
  store i32 %value1, i32* %2, align 4
  %3 = load i32* %2, align 4
  store i32 %3, i32* %local1, align 4
  %4 = load i32* %2, align 4
  %5 = icmp sgt i32 %4, 5
  br i1 %5, label %6, label %10

; <label>:6                                       ; preds = %0
  %7 = load i32* %2, align 4
  %8 = add nsw i32 %7, 10
  store i32 %8, i32* %local1, align 4
  %9 = load i32* %local1, align 4
  store i32 %9, i32* %1
  br label %11

; <label>:10                                      ; preds = %0
  store i32 1, i32* %1
  br label %11

; <label>:11                                      ; preds = %10, %6
  %12 = load i32* %1
  ret i32 %12
}

; Function Attrs: nounwind
define i32 @test73b(i32 %value1) #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %local1 = alloca i32, align 4
  store i32 %value1, i32* %2, align 4
  %3 = load i32* %2, align 4
  store i32 %3, i32* %local1, align 4
  %4 = load i32* %2, align 4
  %5 = icmp sgt i32 %4, 6
  br i1 %5, label %6, label %10

; <label>:6                                       ; preds = %0
  %7 = load i32* %2, align 4
  %8 = add nsw i32 %7, 12
  store i32 %8, i32* %local1, align 4
  %9 = load i32* %local1, align 4
  store i32 %9, i32* %1
  br label %11

; <label>:10                                      ; preds = %0
  store i32 12, i32* %1
  br label %11

; <label>:11                                      ; preds = %10, %6
  %12 = load i32* %1
  ret i32 %12
}

attributes #0 = { nounwind "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-realign-stack" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"Ubuntu clang version 3.6.2-1 (tags/RELEASE_362/final) (based on LLVM 3.6.2)"}
