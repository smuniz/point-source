; ModuleID = '../src/test57.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test57(i32 %var1) #0 {
  %1 = alloca i32, align 4
  %n = alloca i32, align 4
  store i32 %var1, i32* %1, align 4
  %2 = load i32, i32* %1, align 4
  %3 = icmp eq i32 %2, 1
  br i1 %3, label %4, label %14

; <label>:4                                       ; preds = %0
  br label %5

; <label>:5                                       ; preds = %10, %4
  %6 = load i32, i32* %n, align 4
  %7 = add nsw i32 %6, 1
  store i32 %7, i32* %n, align 4
  %8 = load i32, i32* %1, align 4
  %9 = add nsw i32 %8, -1
  store i32 %9, i32* %1, align 4
  br label %10

; <label>:10                                      ; preds = %5
  %11 = load i32, i32* %n, align 4
  %12 = icmp slt i32 %11, 10
  br i1 %12, label %5, label %13

; <label>:13                                      ; preds = %10
  br label %14

; <label>:14                                      ; preds = %13, %0
  %15 = load i32, i32* %1, align 4
  ret i32 %15
}

attributes #0 = { nounwind "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "target-features"="+mmx,+sse,+sse2" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"clang version 3.8.0-2ubuntu4 (tags/RELEASE_380/final)"}
