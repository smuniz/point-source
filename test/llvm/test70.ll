; ModuleID = '../src/test70.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test70(i32 %var1, i32 %var2, i32 %var3, i32 %var4, i32 %var5) #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  %tmp = alloca i32, align 4
  store i32 %var1, i32* %1, align 4
  store i32 %var2, i32* %2, align 4
  store i32 %var3, i32* %3, align 4
  store i32 %var4, i32* %4, align 4
  store i32 %var5, i32* %5, align 4
  %6 = load i32* %1, align 4
  %7 = load i32* %2, align 4
  %8 = and i32 %6, %7
  store i32 %8, i32* %tmp, align 4
  %9 = load i32* %1, align 4
  %10 = load i32* %2, align 4
  %11 = and i32 %9, %10
  %12 = icmp ne i32 %11, 0
  br i1 %12, label %13, label %19

; <label>:13                                      ; preds = %0
  %14 = load i32* %3, align 4
  %15 = load i32* %4, align 4
  %16 = add nsw i32 %14, %15
  %17 = load i32* %tmp, align 4
  %18 = add nsw i32 %16, %17
  store i32 %18, i32* %3, align 4
  br label %23

; <label>:19                                      ; preds = %0
  %20 = load i32* %3, align 4
  %21 = load i32* %5, align 4
  %22 = add nsw i32 %20, %21
  store i32 %22, i32* %3, align 4
  br label %23

; <label>:23                                      ; preds = %19, %13
  %24 = load i32* %3, align 4
  ret i32 %24
}

attributes #0 = { nounwind "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-realign-stack" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"Ubuntu clang version 3.6.2-1 (tags/RELEASE_362/final) (based on LLVM 3.6.2)"}
