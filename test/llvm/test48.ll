; ModuleID = '../src/test48.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test48(i32 %value1, i32 %value2, i32 %value3) #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %local1 = alloca i32, align 4
  store i32 %value1, i32* %1, align 4
  store i32 %value2, i32* %2, align 4
  store i32 %value3, i32* %3, align 4
  store i32 0, i32* %local1, align 4
  %4 = load i32, i32* %1, align 4
  %5 = icmp eq i32 %4, 1
  br i1 %5, label %6, label %13

; <label>:6                                       ; preds = %0
  %7 = load i32, i32* %2, align 4
  %8 = icmp eq i32 %7, 2
  br i1 %8, label %9, label %11

; <label>:9                                       ; preds = %6
  br label %10

; <label>:10                                      ; preds = %17, %9
  store i32 10, i32* %local1, align 4
  store i32 10, i32* %3, align 4
  br label %18

; <label>:11                                      ; preds = %6
  br label %12

; <label>:12                                      ; preds = %16, %11
  store i32 20, i32* %local1, align 4
  store i32 20, i32* %3, align 4
  br label %18

; <label>:13                                      ; preds = %0
  %14 = load i32, i32* %3, align 4
  %15 = icmp eq i32 %14, 3
  br i1 %15, label %16, label %17

; <label>:16                                      ; preds = %13
  br label %12

; <label>:17                                      ; preds = %13
  br label %10

; <label>:18                                      ; preds = %12, %10
  %19 = load i32, i32* %local1, align 4
  ret i32 %19
}

attributes #0 = { nounwind "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "target-features"="+mmx,+sse,+sse2" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"clang version 3.8.0-2ubuntu4 (tags/RELEASE_380/final)"}
