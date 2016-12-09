; ModuleID = '../src/test24.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@mem = internal global [9 x i32] [i32 1, i32 2, i32 3, i32 4, i32 5, i32 6, i32 7, i32 8, i32 9], align 16

; Function Attrs: nounwind
define i32 @test24() #0 {
  %local = alloca i32, align 4
  %n = alloca i32, align 4
  store i32 0, i32* %local, align 4
  store i32 0, i32* %n, align 4
  br label %1

; <label>:1                                       ; preds = %12, %0
  %2 = load i32, i32* %n, align 4
  %3 = sext i32 %2 to i64
  %4 = icmp ult i64 %3, 36
  br i1 %4, label %5, label %15

; <label>:5                                       ; preds = %1
  %6 = load i32, i32* %local, align 4
  %7 = load i32, i32* %n, align 4
  %8 = sext i32 %7 to i64
  %9 = getelementptr inbounds [9 x i32], [9 x i32]* @mem, i64 0, i64 %8
  %10 = load i32, i32* %9, align 4
  %11 = add nsw i32 %6, %10
  store i32 %11, i32* %local, align 4
  br label %12

; <label>:12                                      ; preds = %5
  %13 = load i32, i32* %n, align 4
  %14 = add nsw i32 %13, 1
  store i32 %14, i32* %n, align 4
  br label %1

; <label>:15                                      ; preds = %1
  %16 = load i32, i32* %local, align 4
  ret i32 %16
}

attributes #0 = { nounwind "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "target-features"="+mmx,+sse,+sse2" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"clang version 3.8.0-2ubuntu4 (tags/RELEASE_380/final)"}
