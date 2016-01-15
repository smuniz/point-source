; ModuleID = '../src/test56.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test54(i32 %var1) #0 {
  %1 = alloca i32, align 4
  %n = alloca i32, align 4
  store i32 %var1, i32* %1, align 4
  store i32 0, i32* %n, align 4
  br label %2

; <label>:2                                       ; preds = %15, %0
  %3 = load i32* %1, align 4
  %4 = icmp sgt i32 %3, 10
  br i1 %4, label %5, label %10

; <label>:5                                       ; preds = %2
  %6 = load i32* %n, align 4
  %7 = icmp eq i32 %6, 3
  br i1 %7, label %8, label %9

; <label>:8                                       ; preds = %5
  store i32 20, i32* %1, align 4
  br label %18

; <label>:9                                       ; preds = %5
  br label %10

; <label>:10                                      ; preds = %9, %2
  %11 = load i32* %n, align 4
  %12 = add nsw i32 %11, 1
  store i32 %12, i32* %n, align 4
  %13 = load i32* %1, align 4
  %14 = add nsw i32 %13, -1
  store i32 %14, i32* %1, align 4
  br label %15

; <label>:15                                      ; preds = %10
  %16 = load i32* %n, align 4
  %17 = icmp slt i32 %16, 10
  br i1 %17, label %2, label %18

; <label>:18                                      ; preds = %15, %8
  %19 = load i32* %1, align 4
  ret i32 %19
}

attributes #0 = { nounwind "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-realign-stack" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"Ubuntu clang version 3.6.2-1 (tags/RELEASE_362/final) (based on LLVM 3.6.2)"}
