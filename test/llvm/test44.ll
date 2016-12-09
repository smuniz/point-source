; ModuleID = '../src/test44.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test44(i32 %var1) #0 {
  %1 = alloca i32, align 4
  %n = alloca i32, align 4
  store i32 %var1, i32* %1, align 4
  br label %2

; <label>:2                                       ; preds = %7, %0
  %3 = load i32, i32* %n, align 4
  %4 = add nsw i32 %3, 1
  store i32 %4, i32* %n, align 4
  %5 = load i32, i32* %1, align 4
  %6 = add nsw i32 %5, -1
  store i32 %6, i32* %1, align 4
  br label %7

; <label>:7                                       ; preds = %2
  %8 = load i32, i32* %n, align 4
  %9 = icmp slt i32 %8, 10
  br i1 %9, label %2, label %10

; <label>:10                                      ; preds = %7
  %11 = load i32, i32* %1, align 4
  ret i32 %11
}

attributes #0 = { nounwind "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "target-features"="+mmx,+sse,+sse2" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"clang version 3.8.0-2ubuntu4 (tags/RELEASE_380/final)"}
