; ModuleID = '../src/test45.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test45(i32 %value1) #0 {
  %1 = alloca i32, align 4
  %local1 = alloca i32, align 4
  store i32 %value1, i32* %1, align 4
  %2 = load i32, i32* %1, align 4
  store i32 %2, i32* %local1, align 4
  %3 = load i32, i32* %1, align 4
  %4 = icmp sgt i32 %3, 5
  br i1 %4, label %5, label %14

; <label>:5                                       ; preds = %0
  %6 = load i32, i32* %1, align 4
  %7 = add nsw i32 %6, 10
  store i32 %7, i32* %local1, align 4
  %8 = load i32, i32* %1, align 4
  %9 = icmp sgt i32 %8, 10
  br i1 %9, label %10, label %13

; <label>:10                                      ; preds = %5
  %11 = load i32, i32* %local1, align 4
  %12 = add nsw i32 %11, 11
  store i32 %12, i32* %local1, align 4
  br label %13

; <label>:13                                      ; preds = %10, %5
  br label %14

; <label>:14                                      ; preds = %13, %0
  %15 = load i32, i32* %local1, align 4
  ret i32 %15
}

attributes #0 = { nounwind "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "target-features"="+mmx,+sse,+sse2" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"clang version 3.8.0-2ubuntu4 (tags/RELEASE_380/final)"}
