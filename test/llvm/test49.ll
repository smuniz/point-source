; ModuleID = '../src/test49.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test49(i32 %param1, i32 %param2) #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %n = alloca i32, align 4
  %m = alloca i32, align 4
  store i32 %param1, i32* %1, align 4
  store i32 %param2, i32* %2, align 4
  store i32 0, i32* %n, align 4
  br label %3

; <label>:3                                       ; preds = %35, %0
  %4 = load i32, i32* %n, align 4
  %5 = icmp slt i32 %4, 10
  br i1 %5, label %6, label %38

; <label>:6                                       ; preds = %3
  %7 = load i32, i32* %2, align 4
  %8 = add nsw i32 %7, 10
  store i32 %8, i32* %2, align 4
  %9 = load i32, i32* %n, align 4
  %10 = icmp eq i32 %9, 5
  br i1 %10, label %11, label %14

; <label>:11                                      ; preds = %6
  %12 = load i32, i32* %1, align 4
  %13 = add nsw i32 %12, 2
  store i32 %13, i32* %1, align 4
  br label %14

; <label>:14                                      ; preds = %11, %6
  store i32 0, i32* %m, align 4
  br label %15

; <label>:15                                      ; preds = %21, %14
  %16 = load i32, i32* %m, align 4
  %17 = icmp slt i32 %16, 5
  br i1 %17, label %18, label %24

; <label>:18                                      ; preds = %15
  %19 = load i32, i32* %1, align 4
  %20 = add nsw i32 %19, 5
  store i32 %20, i32* %1, align 4
  br label %21

; <label>:21                                      ; preds = %18
  %22 = load i32, i32* %m, align 4
  %23 = add nsw i32 %22, 1
  store i32 %23, i32* %m, align 4
  br label %15

; <label>:24                                      ; preds = %15
  store i32 0, i32* %m, align 4
  br label %25

; <label>:25                                      ; preds = %31, %24
  %26 = load i32, i32* %m, align 4
  %27 = icmp slt i32 %26, 4
  br i1 %27, label %28, label %34

; <label>:28                                      ; preds = %25
  %29 = load i32, i32* %1, align 4
  %30 = add nsw i32 %29, 4
  store i32 %30, i32* %1, align 4
  br label %31

; <label>:31                                      ; preds = %28
  %32 = load i32, i32* %m, align 4
  %33 = add nsw i32 %32, 1
  store i32 %33, i32* %m, align 4
  br label %25

; <label>:34                                      ; preds = %25
  br label %35

; <label>:35                                      ; preds = %34
  %36 = load i32, i32* %n, align 4
  %37 = add nsw i32 %36, 1
  store i32 %37, i32* %n, align 4
  br label %3

; <label>:38                                      ; preds = %3
  %39 = load i32, i32* %1, align 4
  %40 = load i32, i32* %2, align 4
  %41 = add nsw i32 %39, %40
  ret i32 %41
}

attributes #0 = { nounwind "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "target-features"="+mmx,+sse,+sse2" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"clang version 3.8.0-2ubuntu4 (tags/RELEASE_380/final)"}
